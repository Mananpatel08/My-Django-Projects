from django import forms
from .models import Track, Member

class TrackForm(forms.ModelForm):
    eat_by = forms.ModelMultipleChoiceField(
        queryset=Member.objects.all(),
        widget=forms.CheckboxSelectMultiple,  # Allows multiple selections
        required=True
    )

    class Meta:
        model = Track
        fields = ["date", "tiffin_price", "total_tiffins", "eat_by", "notes"]

        widgets = {
            "date": forms.DateInput(attrs={"type": "date", "class": "form-control"}),
            "tiffin_price": forms.NumberInput(attrs={"class": "form-control"}),
            "total_tiffins": forms.NumberInput(attrs={"class": "form-control"}),
            "notes": forms.Textarea(attrs={"class": "form-control", "rows": 3}),
        }
