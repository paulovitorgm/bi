# Documentação

- [README do projeto](../readme.md): visão geral, instalação local e dados fictícios.
- [Manual rápido do usuário](manual-rapido-usuario.md): uso diário da interface.
- [API REST](api.md): endpoints, autenticação, valores e limitações.
- [Deploy em produção](../deploy/README.md): configuração Windows, Linux, proxy e HTTPS.

## Fluxo recomendado para desenvolvimento

```powershell
poetry install
Copy-Item .envexemple .env
poetry run python manage.py migrate
poetry run python manage.py test
poetry run python manage.py runserver
```

Para gerar uma massa de dados fictícia, consulte os comandos `criar_pessoas` e
`criar_processos` no README do projeto.
