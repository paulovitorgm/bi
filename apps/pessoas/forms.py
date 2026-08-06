from django import forms

from apps.pessoas.models import PessoaModel, UnidadeDeLotacao


class PessoaForm(forms.ModelForm):
    class Meta:
        model = PessoaModel
        fields = ['nome', 'matricula', 'unidade_de_lotacao']
        widgets = {
            'nome': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Digite o nome completo',
                }
            ),
            'matricula': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': '12345678',
                    'oninput': r"this.value=this.value.replace(/\D/g, '').slice(0,8)",
                }
            ),
            'unidade_de_lotacao': forms.Select(attrs={'class': 'form-select tomselect'}),
        }


class UnidadeDeLotacaoForm(forms.ModelForm):
    class Meta:
        model = UnidadeDeLotacao
        fields = ['sigla', 'nome']
        widgets = {
            'sigla': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Sigla'}
            ),
            'nome': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Nome da unidade'}
            ),
        }
