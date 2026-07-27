from django import forms

from apps.controle_de_processos_capro.models import ControleDeProcessosModel


class ControleDeProcessosForm(forms.ModelForm):
    class Meta:
        model = ControleDeProcessosModel
        fields = '__all__'

# class ControleDeProcessosForm(forms.Form):
#     class Meta:
#         model = ControleDeProcessosModel


# from models import MODALIDADE, NATUREZA, ABRANGENCIA, FORMA_DE_APROVACAO,
# ESFERA_ADM, MES, Coordenador
# class ControleDeProcessosModel(forms.Form):
#     processo_sei = forms.CharField(max_length=17)
#     modalidade = forms.ChoiceField(choices=MODALIDADE)
#     natureza = forms.ChoiceField(choices=NATUREZA)
#     abrangencia = forms.ChoiceField(choices=ABRANGENCIA)
#     forma_de_aprovacao = forms.ChoiceField(choices=FORMA_DE_APROVACAO)
#     coordenador = forms.ForeignKey(Coordenador)
#     custos_indiretos = forms.FloatField()
#     esfera_administrativa = forms.IntegerField(choices=ESFERA_ADM)
#     ementa = forms.Textarea(max_length=600)
#     mes_da_aprovacao = forms.IntegerField(choices=MES)
