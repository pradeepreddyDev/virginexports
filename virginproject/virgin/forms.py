from django import forms
from virgin.models import Contacted, Details


class ContactedForm(forms.ModelForm):
    class Meta:
        model = Contacted
        fields = "__all__"


class DetailsForm(forms.ModelForm):
    class Meta:
        model = Contacted
        fields = "__all__"
