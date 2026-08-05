$ErrorActionPreference = 'Stop'

# Execute este script a partir da raiz do projeto. O ambiente Poetry deve
# estar instalado e o arquivo .env deve conter os dados reais de produção.
poetry run python manage.py migrate --noinput
poetry run python manage.py collectstatic --noinput
poetry run waitress-serve --listen=127.0.0.1:8001 base_de_dados_bi.wsgi:application
