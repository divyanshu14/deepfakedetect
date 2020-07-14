from django import forms
from .models import Reason

class ReasonForm(forms.ModelForm):
    class Meta:
        model = Reason
        fields = ['email', 'age', 'gender', 'ethnicity', 'video_type', 'reason_text', 'reason_keywords']
