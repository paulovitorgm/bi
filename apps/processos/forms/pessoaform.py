from django import forms

from apps.pessoas.models import PessoaModel


class PessoaForm(forms.ModelForm):
    class Meta:
        model = PessoaModel
        fields = '__all__'
        widgets = {
            'nome': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Nome Completo'}
            ),
        }
