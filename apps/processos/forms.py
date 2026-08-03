from django import forms

from apps.processos.models import (
    EntidadeParceira,
    ItemPlanoDespesa,
    Modalidade,
    Natureza,
    PessoaModel,
    ProcessoProjeto,
    TipoDespesa,
    Unidade,
)


class ProcessoProjetoForm(forms.ModelForm):
    class Meta:
        model = ProcessoProjeto
        fields = '__all__'
        labels = {
            'processo': 'Processo SEI',
            'numero_convenio': 'Número do Convênio',
            'nome_do_processo': 'Nome do Processo',
            'ementa': 'Ementa',
            'participes_texto': 'Partícipes do projeto',
            'tipo_instrumento': 'Tipo de instrumento',
            'esfera_administrativa': 'Esfera Administrativa',
            'unidade_interessada': 'Unidade Interessada',
            'modalidade': 'Modalidade',
            'natureza': 'Natureza',
            'abrangencia': 'Abrangência',
            'entidade_parceira': 'Entidade Parceira',
            'coordenador': 'Coordenador(a)',
            'supervisor_academico': 'Supervisor Acadêmico',
            'relator': 'Relator(a)',
            'substituto': 'Substituto(a)',
            'valor_total': 'Valor total do projeto',
            'valor_inicial': 'Valor inicial',
            'custos_indiretos': 'Custos indiretos',
            'dt_inicio': 'Data de Início',
            'dt_termino': 'Data de Término',
            'dt_assinatura': 'Data da Assinatura',
            'forma_aprovacao': 'Forma de aprovação',
            'ods_onu': 'ODS da ONU',
            'pste': 'PSTE',
        }
        widgets = {
            'processo': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': '23106092037202530',
                    'inputmode': 'numeric',
                    'pattern': '[0-9]*',
                    'oninput': 'this.value=this.value.replace(/\\D/g,"")',
                }
            ),
            'numero_convenio': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Número do Convênio'}
            ),
            'nome_do_processo': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Título do processo',
                }
            ),
            'ementa': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Resumo ou ementa do projeto',
                    'style': 'height: 100px',
                }
            ),
            'participes_texto': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Descrição dos partícipes',
                    'style': 'height: 100px',
                }
            ),
            'forma_aprovacao': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': ''}
            ),
            # Selects (Dropdowns)
            'tipo_instrumento': forms.Select(
                attrs={
                    'class': 'form-select tomselect',
                }
            ),
            'esfera_administrativa': forms.Select(
                attrs={
                    'class': 'form-select tomselect',
                }
            ),
            'unidade_interessada': forms.SelectMultiple(
                attrs={'class': 'form-select tomselect', 'multiple': 'multiple'}
            ),
            'modalidade': forms.SelectMultiple(
                attrs={'class': 'form-select tomselect', 'multiple': 'multiple'}
            ),
            'natureza': forms.SelectMultiple(
                attrs={'class': 'form-select tomselect', 'multiple': 'multiple'}
            ),
            'abrangencia': forms.Select(
                attrs={
                    'class': 'form-select tomselect',
                }
            ),
            'entidade_parceira': forms.Select(
                attrs={
                    'class': 'form-select tomselect',
                }
            ),
            # Selects para Pessoas
            'coordenador': forms.Select(
                attrs={
                    'class': 'form-select tomselect',
                }
            ),
            'supervisor_academico': forms.Select(
                attrs={
                    'class': 'form-select tomselect',
                }
            ),
            'relator': forms.Select(
                attrs={
                    'class': 'form-select tomselect',
                }
            ),
            'substituto': forms.Select(
                attrs={
                    'class': 'form-select tomselect',
                }
            ),
            # Valores Monetários
            'valor_total': forms.NumberInput(
                attrs={'class': 'form-control', 'placeholder': '0.00', 'step': '0.01'}
            ),
            'valor_inicial': forms.NumberInput(
                attrs={'class': 'form-control', 'placeholder': '0.00', 'step': '0.01'}
            ),
            'custos_indiretos': forms.NumberInput(
                attrs={'class': 'form-control', 'placeholder': '0.00', 'step': '0.01'}
            ),
            # Datas
            'dt_inicio': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'dt_termino': forms.DateInput(
                attrs={'class': 'form-control', 'type': 'date'}
            ),
            'dt_assinatura': forms.DateInput(
                attrs={'class': 'form-control', 'type': 'date'}
            ),
            'ods_onu': forms.Select(
                attrs={
                    'class': 'form-select tomselect',
                }
            ),
            # Checkboxes (Switches do Bootstrap)
            'pste': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

        def clean(self):
            cleaned_data = super().clean()
            dt_inicio = cleaned_data.get('dt_inicio')
            dt_termino = cleaned_data.get('dt_termino')

            # Data de término não pode ser anterior à data de início
            if dt_inicio and dt_termino and dt_termino < dt_inicio:
                raise forms.ValidationError(
                    'A data de término não pode ser anterior à data de início.'
                )


# ==========================================
# FORMULÁRIO: ITENS DO PLANO DE DESPESA
# ==========================================


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


# ==========================================
# FORMULÁRIOS DE TABELAS DE DOMÍNIO
# ==========================================


class UnidadeForm(forms.ModelForm):
    class Meta:
        model = Unidade
        fields = ['sigla', 'nome']
        widgets = {
            'sigla': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Sigla'}
            ),
            'nome': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Nome da Unidade'}
            ),
        }


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


class PessoaForm(forms.ModelForm):
    class Meta:
        model = PessoaModel
        fields = '__all__'
        widgets = {
            'nome': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Nome Completo'}
            ),
        }


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


class NaturezaForm(forms.ModelForm):
    class Meta:
        model = Natureza
        fields = ['nome']

        widgets = {
            'nome': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Nome da natureza',
                }
            )
        }
