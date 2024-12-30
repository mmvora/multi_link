from django import forms
from .models import Link


class LinkForm(forms.ModelForm):
    custom_category = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={"placeholder": "Enter custom category"}),
    )

    class Meta:
        model = Link
        fields = ["url", "category", "title", "description", "custom_category"]
