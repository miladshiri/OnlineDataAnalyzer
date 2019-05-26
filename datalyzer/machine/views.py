from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from .forms import UploadFileForm
from pandas import read_csv, DataFrame, read_excel, Series
from .models import Data


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
