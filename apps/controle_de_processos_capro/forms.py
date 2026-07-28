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
