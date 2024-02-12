from typing import Any
from django import forms
from django.core.exceptions import ValidationError
from . import models


class ContactForm(forms.ModelForm):
    picture = forms.ImageField(
        widget=forms.FileInput(
            attrs={
                'accept': 'image/*'
            }
        )
    )

    class Meta:
        model = models.Contact
        fields = (
            'first_name',
            'last_name',
            'phone',
            'email',
            'description',
            'category',
            'picture',
        )

    def clean(self) -> dict[str, Any]:
        cleaned_data = self.cleaned_data
        first_name = cleaned_data.get('first_name')
        last_name = cleaned_data.get('last_name')

        if first_name == last_name:
            msg = ValidationError(
                'last name não pode ser igual ao first name.',
                code='invalid',
            )
            self.add_error('last_name', msg)

        return super().clean()

    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')

        if len(first_name) <= 3:
            self.add_error(
                'first_name',
                ValidationError(
                    'Campo deve ter ao menos 4 caracteres.',
                    code='invalid'
                )
            )

        return first_name
