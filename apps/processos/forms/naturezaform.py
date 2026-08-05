from django import forms

from apps.processos.models.natureza import Natureza


class NaturezaForm(forms.ModelForm):
    class Meta:
        model = Natureza
        fields = ['nome']

        widgets = {
            'nome': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Nome da natureza',
                }
            )
        }
