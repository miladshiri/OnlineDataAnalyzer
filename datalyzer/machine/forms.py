from django import forms
from .models import Data, METHOD_CHOICES, Machine, METHOD_PARAMS, Train


class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    description = forms.CharField(max_length=300)
    file = forms.FileField()
    public = forms.BooleanField(required=False)
    column_title_first_row = forms.BooleanField(required=False, )

    def clean(self):
        cleaned_data = super(UploadFileForm, self).clean()
        file = cleaned_data['file']

        if file:
            filename = file.name
            file_format = filename.split('.')[-1]
            upload_types = ['txt', 'xls', 'csv']
            if file_format not in upload_types:
                raise forms.ValidationError("File is not a {} file.".format('/'.join(upload_types)))


class DataModelChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.name


class SelectModelForm(forms.Form):
    method = forms.ChoiceField(choices=METHOD_CHOICES)


def machine_config_form_factory(method_name):
    base_fields = ['name', 'description']

    class MachineConfigForm(forms.ModelForm):
        class Meta:
            model = Machine
            fields = base_fields + METHOD_PARAMS[method_name]

    return MachineConfigForm


class MachineCreateForm(forms.ModelForm):

    class Meta:
        model = Machine
        exclude = ['user', 'method']


class TrainModelForm(forms.ModelForm):
    label = forms.IntegerField(label='Label Column', initial=0)

    class Meta:
        model = Train
        exclude = ['user', 'trained_model', 'is_trained']

    def __init__(self, user, *args, **kwargs):
        super(TrainModelForm, self).__init__(*args, **kwargs)
        self.fields['data'].queryset = Data.objects.filter(user=user)
        self.fields['machine'].queryset = Machine.objects.filter(user=user)


class FitModelForm(forms.ModelForm):

    class Meta:
        model = Machine
        exclude = ['name']


