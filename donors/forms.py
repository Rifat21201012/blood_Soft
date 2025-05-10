from django import forms
from .models import Donor


class DonorForm(forms.ModelForm):
    class Meta:
        model = Donor
        fields = [
            "blood_group",
            "quantity",
            "when_needed",
            "contact_number",
            "description",
            "disease_description",  # <-- New field
        ]
        widgets = {
            'when_needed': forms.DateTimeInput(
                attrs={'type': 'datetime-local'},
                format='%Y-%m-%dT%H:%M'
            ),
        }

    def _init_(self, *args, **kwargs):
        super(DonorForm, self)._init_(*args, **kwargs)
        self.fields['when_needed'].input_formats = ['%Y-%m-%dT%H:%M']