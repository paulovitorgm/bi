from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.base.urls')),
    path('controle-de-processos/', include('apps.controle_de_processos_capro.urls')),
]
