from django import forms
from django.forms import inlineformset_factory

from apps.processos.models.processoprojeto import ProcessoProjeto
from apps.processos.models.termosadtivos import TermosAdtivos


class ProcessoProjetoForm(forms.ModelForm):
    class Meta:
        model = ProcessoProjeto
        fields = [
            'processo',
            'numero_convenio',
            'nome_do_processo',
            'ementa',
            'participes',
            'tipo_instrumento',
            'esfera_administrativa',
            'abrangencia',
            'unidade_interessada',
            'modalidade',
            'natureza',
            'entidade_parceira',
            'coordenador',
            'supervisor_academico',
            'relator',
            'substituto',
            'valor_inicial',
            'valor_total',
            'custos_indiretos',
            'dt_assinatura',
            'dt_inicio',
            'dt_termino',
            'ods_onu',
        ]
        labels = {
            'processo': 'Processo SEI',
            'numero_convenio': 'Número do convênio',
            'nome_do_processo': 'Nome do processo',
            'participes': 'Partícipes do projeto',
            'tipo_instrumento': 'Tipo de instrumento',
            'unidade_interessada': 'Unidade interessada',
            'entidade_parceira': 'Entidade parceira',
            'dt_inicio': 'Data de início',
            'dt_termino': 'Data de término',
            'dt_assinatura': 'Data da assinatura',
            'ods_onu': 'ODS da ONU',
        }
        widgets = {
            'processo': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'inputmode': 'numeric',
                    'pattern': '[0-9]*',
                }
            ),
            'numero_convenio': forms.TextInput(attrs={'class': 'form-control'}),
            'nome_do_processo': forms.TextInput(attrs={'class': 'form-control'}),
            'ementa': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'participes': forms.SelectMultiple(attrs={'class': 'form-select tomselect'}),
            'tipo_instrumento': forms.Select(attrs={'class': 'form-select tomselect'}),
            'esfera_administrativa': forms.Select(attrs={'class': 'form-select'}),
            'abrangencia': forms.Select(attrs={'class': 'form-select tomselect'}),
            'unidade_interessada': forms.SelectMultiple(
                attrs={'class': 'form-select tomselect'}
            ),
            'modalidade': forms.SelectMultiple(attrs={'class': 'form-select tomselect'}),
            'natureza': forms.SelectMultiple(attrs={'class': 'form-select tomselect'}),
            'entidade_parceira': forms.Select(attrs={'class': 'form-select tomselect'}),
            'coordenador': forms.Select(attrs={'class': 'form-select tomselect'}),
            'supervisor_academico': forms.Select(
                attrs={'class': 'form-select tomselect'}
            ),
            'relator': forms.Select(attrs={'class': 'form-select tomselect'}),
            'substituto': forms.Select(attrs={'class': 'form-select tomselect'}),
            'valor_total': forms.NumberInput(
                attrs={'class': 'form-control', 'step': '0.01'}
            ),
            'valor_inicial': forms.NumberInput(
                attrs={'class': 'form-control', 'step': '0.01'}
            ),
            'custos_indiretos': forms.NumberInput(
                attrs={'class': 'form-control', 'step': '0.01'}
            ),
            'dt_inicio': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'dt_termino': forms.DateInput(
                attrs={
                    'class': 'form-control bg-body-secondary',
                    'type': 'date',
                    'readonly': True,
                }
            ),
            'dt_assinatura': forms.DateInput(
                attrs={'class': 'form-control', 'type': 'date'}
            ),
            'ods_onu': forms.Select(attrs={'class': 'form-select tomselect'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # O total é calculado no servidor e apresentado apenas para conferência.
        self.fields['valor_total'].disabled = True
        self.fields['valor_total'].required = False

    def clean(self):
        cleaned_data = super().clean()
        dt_assinatura = cleaned_data.get('dt_assinatura')
        dt_inicio = cleaned_data.get('dt_inicio')
        dt_termino = cleaned_data.get('dt_termino')

        if dt_assinatura and dt_inicio and dt_inicio < dt_assinatura:
            self.add_error(
                'dt_inicio',
                'A data de início não pode ser anterior à data de assinatura.',
            )
        if dt_assinatura and dt_termino and dt_termino < dt_assinatura:
            self.add_error(
                'dt_termino',
                'A data de término não pode ser anterior à data de assinatura.',
            )
        if dt_inicio and dt_termino and dt_termino < dt_inicio:
            self.add_error(
                'dt_termino',
                'A data de término não pode ser anterior à data de início.',
            )

        responsaveis = {
            nome: cleaned_data.get(nome)
            for nome in (
                'coordenador',
                'supervisor_academico',
                'relator',
                'substituto',
            )
        }
        por_pessoa = {}
        for papel, pessoa in responsaveis.items():
            if pessoa is not None:
                por_pessoa.setdefault(pessoa.pk, []).append(papel)
        for papeis in por_pessoa.values():
            if len(papeis) > 1:
                mensagem = (
                    'A mesma pessoa não pode exercer mais de um papel neste processo.'
                )
                for papel in papeis:
                    self.add_error(papel, mensagem)

        return cleaned_data


class TermoAditivoInlineForm(forms.ModelForm):
    class Meta:
        model = TermosAdtivos
        fields = ['termo', 'dt_assinatura', 'dt_termino', 'valor']
        widgets = {
            'termo': forms.TextInput(attrs={'class': 'form-control'}),
            'dt_assinatura': forms.DateInput(
                attrs={'class': 'form-control', 'type': 'date'}
            ),
            'dt_termino': forms.DateInput(
                attrs={
                    'class': 'form-control bg-body-secondary',
                    'type': 'date',
                    'readonly': True,
                }
            ),
            'valor': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        dt_assinatura = cleaned_data.get('dt_assinatura')
        dt_termino = cleaned_data.get('dt_termino')
        if dt_assinatura and dt_termino and dt_assinatura > dt_termino:
            self.add_error(
                'dt_termino',
                'A assinatura deve ser anterior ou igual à data de término.',
            )
        return cleaned_data


TermoAditivoFormSet = inlineformset_factory(
    ProcessoProjeto,
    TermosAdtivos,
    form=TermoAditivoInlineForm,
    extra=3,
    can_delete=True,
)
