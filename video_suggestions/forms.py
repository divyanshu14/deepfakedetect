from django import forms
from .models import Reason

class ReasonForm(forms.ModelForm):
    class Meta:
        model = Reason
        fields = ['reason_text']
