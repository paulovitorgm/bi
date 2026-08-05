from django import forms

from apps.processos.models.tipodespesa import TipoDespesa


class TipoDespesaForm(forms.ModelForm):
    class Meta:
        model = TipoDespesa
        fields = ['descricao']
        widgets = {
            'descricao': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Descrição do Tipo de Despesa',
                }
            ),
        }
