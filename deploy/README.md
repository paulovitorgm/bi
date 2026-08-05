# Operação em produção (sem contêiner)

Para uma implantação definitiva, execute o Django com um servidor WSGI, como
o **Waitress**, na porta local `8001`. Mantenha essa porta inacessível pela
rede; exponha somente o proxy web (Nginx ou IIS) em `80/443`.

## Configuração inicial

1. Instale Python, Poetry e PostgreSQL no servidor. Crie o banco e um usuário
   PostgreSQL com acesso somente ao banco desta aplicação.
2. Copie `.envexemple` para `.env` e preencha todos os valores reais. Em
   produção, mantenha `DEBUG=False`, informe o nome DNS/IP em `ALLOWED_HOSTS`
   e gere uma `SECRET_KEY` nova. O arquivo `.env` não é enviado ao Git.
3. Instale os pacotes já definidos no projeto e aplique a base:

   ```powershell
   poetry install --only main
   poetry run python manage.py migrate --noinput
   poetry run python manage.py collectstatic --noinput
   ```

4. Quando o servidor tiver acesso a um repositório de pacotes (ou quando a
   equipe fornecer o instalador offline), instale o Waitress e inicie-o:

   ```powershell
   poetry run pip install waitress==3.0.2
   poetry run waitress-serve --listen=127.0.0.1:8001 base_de_dados_bi.wsgi:application
   ```

## Windows Server

Use `deploy/windows/iniciar-producao.ps1` para o teste manual. Para manter o
processo ativo após reinicializações, registre esse comando como um serviço no
gerenciador de serviços já adotado pela organização (por exemplo, NSSM ou o
Agendador de Tarefas). Configure o serviço para iniciar automaticamente e use
uma conta de serviço com acesso apenas à pasta da aplicação e ao banco.

## Linux

Crie o usuário de serviço `bi`, instale o projeto em `/opt/base-dados-bi` e
ajuste os caminhos em `deploy/linux/base-dados-bi.service` se necessário.
Copie o arquivo para `/etc/systemd/system/`, então habilite e inicie:

```bash
sudo systemctl daemon-reload
sudo systemctl enable --now base-dados-bi
```

## Proxy e HTTPS

Use `deploy/nginx/base-dados-bi.conf` como base para o Nginx. Troque
`servidor-bi.interno` pelo DNS real. Quando HTTPS estiver pronto, configure o
certificado no proxy e mantenha no `.env`:

```env
SECURE_SSL_REDIRECT=True
SESSION_COOKIE_SECURE=True
CSRF_COOKIE_SECURE=True
CSRF_TRUSTED_ORIGINS=https://seu-dns
```

Em uma rede interna sem HTTPS, mantenha essas três opções como `False` e não
defina `CSRF_TRUSTED_ORIGINS` até haver um certificado.

O bloco `/static/` do Nginx aponta para `staticfiles`, criado pelo comando
`collectstatic`. Ajuste o caminho `alias` caso a aplicação não esteja em
`/opt/base-dados-bi`.
