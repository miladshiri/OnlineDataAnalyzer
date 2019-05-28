from django.shortcuts import render, redirect
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from .forms import UploadFileForm, TrainModelForm, SelectModelForm, FitModelForm, \
    machine_config_form_factory, MachineCreateForm
from pandas import read_csv, DataFrame, read_excel, Series
from .models import Data
from django.forms import modelform_factory
from django.urls import reverse
from urllib.parse import urlencode
from django.forms.models import model_to_dict

def upload_data(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():

            data_file = request.FILES['file']
            file_format = data_file.name.split('.')[-1]

            if file_format in ['txt', 'csv']:
                data_df = read_csv(data_file, sep=',', header=None)
            elif file_format in ['xls', 'xlsx']:
                data_df = read_excel(data_file, header=None)
            else:
                data_df = DataFrame([])

            features = Series(data_df.columns)
            if form.cleaned_data['column_title_first_row']:
                features = data_df.iloc[0, :]
                data_df = data_df.drop(data_df.index[0])

            data_obj = Data(data_json=str(data_df.to_json()),
                            features_json=str(features.to_json()),
                            user=request.user,
                            name=form.cleaned_data['title'],
                            description=form.cleaned_data['description'],
                            is_public=form.cleaned_data['public'])
            data_obj.save()

            return render(request, 'machine/upload_successful.html')

    else:
        form = UploadFileForm()
    return render(request, 'machine/upload_page.html', {'form' : form})


def select_method(request):
    if request.method == 'POST':
        form = SelectModelForm(request.POST)
        if form.is_valid():
            base_url = reverse('machine:config_machine')
            query_string = urlencode({'method': form.cleaned_data['method']})
            url = '{}?{}'.format(base_url, query_string)
            return redirect(url)
    else:
        form = SelectModelForm()
    return render(request, 'machine/select_method.html', {'form': form})


def config_machine(request):
    method_name = request.GET.get('method')
    if request.method == 'POST':
        form = MachineCreateForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.method = method_name
            obj.save()

            return redirect('machine:model_data')

    else:
        form = machine_config_form_factory(method_name)

    return render(request, 'machine/config_machine.html', {'form': form()})


def model_data(request):
    if request.method == 'POST':
        form = TrainModelForm(request.user, request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.save()
        return render(request, 'machine/train_model.html', {'form': form})
    else:
        form = TrainModelForm(request.user)
    return render(request, 'machine/train_model.html', {'form': form})
