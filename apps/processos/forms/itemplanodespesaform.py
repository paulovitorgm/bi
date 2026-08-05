from django import forms

from apps.processos.models.itemplanodespesa import ItemPlanoDespesa


class ItemPlanoDespesaForm(forms.ModelForm):
    class Meta:
        model = ItemPlanoDespesa
        fields = ['tipo_despesa', 'valor']
        widgets = {
            'tipo_despesa': forms.Select(attrs={'class': 'form-select tomselect'}),
            'valor': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Valor (R$)',
                    'step': '0.01',
                }
            ),
        }
