from django import forms

from apps.controle_de_processos_capro.models.controle_de_processos import (
    ControleDeProcessosModel,
)
from apps.controle_de_processos_capro.models.coordenador import CoordenadorModel


class BootstrapModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for nome, campo in self.fields.items():
            widget = campo.widget

            if isinstance(widget, forms.Select):
                widget.attrs['class'] = 'form-select'

                if nome == 'coordenador':
                    widget.attrs['class'] += ' tomselect'

            else:
                widget.attrs['class'] = 'form-control'


class ControleDeProcessosForm(BootstrapModelForm):
    class Meta:
        model = ControleDeProcessosModel
        fields = '__all__'


class CoordenadorForm(BootstrapModelForm):
    class Meta:
        model = CoordenadorModel
        fields = '__all__'


class DeletarProcesso(forms.Form):
    processo = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class BuscarProcessoForm(forms.Form):
    processo_sei = forms.CharField(
        label='Número do processo',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': '60704.986946/1810-15',
                'inputmode': 'numeric',
                'oninput': r"this.value=this.value.replace(/\D/g, '').slice(0,17)",
            }
        ),
    )

    def clean_processo_sei(self):
        processo = self.cleaned_data['processo_sei']
        self.PROCESSO_SEI_TAMANHO = 17
        if len(processo) != self.PROCESSO_SEI_TAMANHO:
            raise forms.ValidationError(
                'O número do processo deve possuir 17 dígitos.'
            )
        return processo
