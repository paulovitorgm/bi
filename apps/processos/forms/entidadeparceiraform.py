from django import forms

from apps.processos.models.entidadeparceira import EntidadeParceira


class EntidadeParceiraForm(forms.ModelForm):
    class Meta:
        model = EntidadeParceira
        fields = [
            'sigla',
            'nome',
            'cnpj_cpf',
            'publico_privado',
        ]

        labels = {
            'sigla': 'Sigla',
            'nome': 'Nome da Entidade',
            'cnpj_cpf': 'CNPJ/CPF',
            'publico_privado': 'Natureza',
        }

        widgets = {
            'sigla': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Ex: Finatec'}
            ),
            'nome': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Nome completo da entidade',
                }
            ),
            'cnpj_cpf': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'CNPJ ou CPF'}
            ),
            'publico_privado': forms.Select(attrs={'class': 'form-select tomselect'}),
        }
