# API REST

A API está disponível em `/api/v1/` e aceita JSON. Ela exige um usuário do
sistema autenticado, por sessão ou pelo cabeçalho HTTP Basic Authentication.

Principais rotas:

- `GET, POST /api/v1/processos/`
- `GET, PUT, PATCH, DELETE /api/v1/processos/{numero_do_processo}/`
- `GET, POST /api/v1/termos-aditivos/`
- `GET, PUT, PATCH, DELETE /api/v1/termos-aditivos/{id}/`
- `GET /api/v1/pessoas/`, `abrangencias/`, `entidades-parceiras/`,
  `modalidades/`, `naturezas/`, `participes/`, `tipos-instrumento/` e
  `unidades/`

O campo `valor_total` é somente leitura. O sistema calcula seu valor como
`valor_inicial + soma dos termos aditivos` sempre que o processo ou um termo é
alterado.

Para permitir que um front-end hospedado em outro endereço consuma a API pelo
navegador, configure no `.env`:

```env
CORS_ALLOWED_ORIGINS=https://novo-front.exemplo.gov.br,http://localhost:3000
```
