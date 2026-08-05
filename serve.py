from waitress import serve
from base_de_dados_bi.wsgi import application


serve(
    application,
    host="0.0.0.0",
    port=80,
    threads=8,
)

