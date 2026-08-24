# API REST

A API está disponível em `/api/v1/`, aceita JSON e exige autenticação. São
aceitos `SessionAuthentication` e `BasicAuthentication`. Usuários anônimos
recebem `401` em vez de serem redirecionados para a tela HTML de login.

## Endpoints

Processos usam o número do processo como identificador na URL:

- `GET, POST /api/v1/processos/`
- `GET, PUT, PATCH, DELETE /api/v1/processos/{processo}/`
- `GET, POST /api/v1/termos-aditivos/`
- `GET, PUT, PATCH, DELETE /api/v1/termos-aditivos/{id}/`

Os cadastros abaixo são somente leitura e oferecem `GET` para lista e detalhe:

`pessoas`, `abrangencias`, `entidades-parceiras`, `modalidades`, `naturezas`,
`participes`, `tipos-instrumento` e `unidades`.

As listas usam paginação por página. O tamanho padrão é configurado no servidor;
o parâmetro `page_size` não está habilitado atualmente.

Busca textual e ordenação por query string ainda não estão habilitadas na API.
Os atributos `search_fields` e `ordering_fields` existentes no código não
alteram o comportamento sem os respectivos filtros do Django REST Framework.

## Valores e importação em massa

`valor_total` é somente leitura e é calculado como:

`valor_inicial + soma dos termos aditivos`.

Depois de usar `bulk_create` ou `QuerySet.update()` em uma importação, execute
`recalcular_valores_totais(ids_dos_processos)` na mesma operação de carga. A
função está em `apps.processos.services`.

## CORS

Para um frontend hospedado em outro endereço, configure explicitamente as
origens permitidas no `.env`:

```env
CORS_ALLOWED_ORIGINS=https://novo-front.exemplo.gov.br,http://localhost:3000
```

O middleware responde a preflight `OPTIONS` da API e permite os headers
`Authorization` e `Content-Type`. A origem não incluída nessa lista não recebe
headers CORS. O suporte a credenciais e a `X-CSRFToken` ainda não está
implementado.

## Limitações atuais

- Cadastros auxiliares são somente leitura pela API.
- Despesas não possuem endpoints REST próprios.
- Operações em massa exigem o recálculo explícito dos totais.
