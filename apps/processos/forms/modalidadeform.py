from django import forms

from apps.processos.models.modalidade import Modalidade


class ModalidadeForm(forms.ModelForm):
    class Meta:
        model = Modalidade
        fields = ['nome']

        labels = {
            'nome': 'Nome da Modalidade',
        }

        widgets = {
            'nome': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Nome da modalidade'}
            ),
        }
