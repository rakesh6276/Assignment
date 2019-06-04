from django.forms import forms, FileField
from django.core.exceptions import ValidationError
import os

#function read only .xlsx and xls files
def validate_file_extension(value):
    ext = os.path.splitext(value.name)[1]
    if not ext.lower() in ['.xlsx', '.xls']:
        raise ValidationError(u'Unsupported file extension')

class ExcelUploadForm(forms.Form):
    excel_file = FileField()