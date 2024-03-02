from django import forms
from .models import Scout


class ScoutForm(forms.ModelForm):
    # Custom fields
    current_patrol = forms.CharField(max_length=200, required=False)
    date_started_in_patrol = forms.DateField(required=False)

    class Meta:
        model = Scout
        fields = ['first_name', 'last_name', 'ssa_id', 'dob', 'current_patrol', 'date_started_in_patrol']
