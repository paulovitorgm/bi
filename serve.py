print("Importando Waitress...")

from waitress import serve

print("Importando WSGI...")

from base_de_dados_bi.wsgi import application

print("Iniciando servidor...")

serve(
    application,
    host="0.0.0.0",
    port=8001,
    threads=8,
)

print("Servidor encerrado.")