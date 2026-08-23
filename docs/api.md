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

Todas as listas são paginadas. Use `page` e `page_size` conforme a configuração
do servidor. Nos endpoints de processos e termos aditivos, use:

- `?search=termo` para busca textual;
- `?ordering=campo` para ordenar ascendente;
- `?ordering=-campo` para ordenar descendente.

Os campos permitidos para ordenação são `processo`, `dt_inicio`, `dt_termino`
e `valor_total` em processos, e `termo`, `dt_assinatura`, `dt_termino` e
`valor` em termos aditivos.

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

O middleware responde a preflight `OPTIONS` da API e permite credenciais,
`Authorization`, `Content-Type` e `X-CSRFToken`. A origem não incluída nessa
lista não recebe headers CORS.
