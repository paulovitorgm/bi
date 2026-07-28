from django import template

register = template.Library()
PROCESSO_SEI_TAMANHO = 17


@register.filter(name='sei_mask')
def mascara_sei(value):
    string_value = str(value).strip()
    if string_value.isdigit():
        string_value = string_value.zfill(PROCESSO_SEI_TAMANHO)
    if len(string_value) == PROCESSO_SEI_TAMANHO:
        parte1 = string_value[:5]
        parte2 = string_value[5:11]
        parte3 = string_value[11:15]
        parte4 = string_value[15:]
        return f'{parte1}.{parte2}/{parte3}-{parte4}'

    return value
