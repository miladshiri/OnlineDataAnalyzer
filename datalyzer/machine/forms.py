from django import forms


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

