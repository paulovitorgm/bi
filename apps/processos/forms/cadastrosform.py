from django import forms

from apps.processos.models.abrangencia import Abrangencia
from apps.processos.models.participesmodel import ParticipesModel
from apps.processos.models.termosadtivos import TermosAdtivos
from apps.processos.models.tipoinstrumento import TipoInstrumento


class AbrangenciaForm(forms.ModelForm):
    class Meta:
        model = Abrangencia
        fields = ['nome']
        widgets = {'nome': forms.TextInput(attrs={'class': 'form-control'})}


class ParticipeForm(forms.ModelForm):
    class Meta:
        model = ParticipesModel
        fields = ['sigla', 'nome']
        widgets = {
            'sigla': forms.TextInput(attrs={'class': 'form-control'}),
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
        }


class TipoInstrumentoForm(forms.ModelForm):
    class Meta:
        model = TipoInstrumento
        fields = ['nome']
        widgets = {'nome': forms.TextInput(attrs={'class': 'form-control'})}


class TermoAditivoForm(forms.ModelForm):
    class Meta:
        model = TermosAdtivos
        fields = ['termo', 'dt_assinatura', 'dt_termino', 'valor']
        widgets = {
            'termo': forms.TextInput(attrs={'class': 'form-control'}),
            'dt_assinatura': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'dt_termino': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'valor': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
        }
