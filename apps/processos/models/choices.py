from django.db import models


class PublicoPrivado(models.TextChoices):
    PUBLICO = 'Publico', 'Publico'
    PRIVADO = 'Privado', 'Privado'


class OdsOnuChoices(models.TextChoices):
    ODS_1 = '1', '1. Erradicação da Pobreza'
    ODS_2 = '2', '2. Fome Zero e Agricultura Sustentável'
    ODS_3 = '3', '3. Saúde e Bem-Estar'
    ODS_4 = '4', '4. Educação de Qualidade'
    ODS_5 = '5', '5. Igualdade de Gênero'
    ODS_6 = '6', '6. Água Potável e Saneamento'
    ODS_7 = '7', '7. Energia Limpa e Acessível'
    ODS_8 = '8', '8. Trabalho Decente e Crescimento Econômico'
    ODS_9 = '9', '9. Indústria, Inovação e Infraestrutura'
    ODS_10 = '10', '10. Redução das Desigualdades'
    ODS_11 = '11', '11. Cidades e Comunidades Sustentáveis'
    ODS_12 = '12', '12. Consumo e Produção Responsáveis'
    ODS_13 = '13', '13. Ação Contra a Mudança Global do Clima'
    ODS_14 = '14', '14. Vida na Água'
    ODS_15 = '15', '15. Vida Terrestre'
    ODS_16 = '16', '16. Paz, Justiça e Instituições Eficazes'
    ODS_17 = '17', '17. Parcerias e Meios de Implementação'


class EsferaAdministrativaChoices(models.TextChoices):
    FEDERAL = 'Federal', 'Federal'
    ESTADUAL = 'Estadual', 'Estadual'
    MUNICIPAL = 'Municipal', 'Municipal'
    INICIATIVA_PRIVADA = 'Iniciativa Privada', 'Iniciativa Privada'
    INTERNACIONAL = 'Internacional', 'Internacional'


class TipoInstrumentoChoices(models.TextChoices):
    CONVENIO = 'Convênio', 'Convênio'
    CONTRATO = 'Contrato', 'Contrato'
    ACORDO_COOPERACAO = 'Acordo de Cooperação', 'Acordo de Cooperação'
    TERMO_COMPROMISSO = 'Termo de Compromisso', 'Termo de Compromisso'
    TERMO_EXECUCAO = (
        'Termo de Execução Descentralizada',
        'Termo de Execução Descentralizada',
    )
    TERMO_OUTORGA = 'Termo de Outorga', 'Termo de Outorga'
