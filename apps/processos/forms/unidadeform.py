from django import forms

from apps.processos.models.unidade import Unidade


class UnidadeForm(forms.ModelForm):
    class Meta:
        model = Unidade
        fields = ['sigla', 'nome']
        widgets = {
            'sigla': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Sigla'}
            ),
            'nome': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Nome da Unidade'}
            ),
        }
