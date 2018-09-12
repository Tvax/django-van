from django import forms
from uploads.core.models import Document

class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ('title', 'version', 'file',)  