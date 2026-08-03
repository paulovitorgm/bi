from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.base.urls')),
    path('pessoas/', include('apps.pessoas.urls')),
    path('processos/', include('apps.processos.urls')),
]
