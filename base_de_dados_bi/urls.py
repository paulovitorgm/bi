from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import include, path

handler400 = 'base_de_dados_bi.error_views.bad_request'
handler403 = 'base_de_dados_bi.error_views.permission_denied'
handler404 = 'base_de_dados_bi.error_views.page_not_found'
handler500 = 'base_de_dados_bi.error_views.server_error'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.base.urls')),
    path('pessoas/', include('apps.pessoas.urls')),
    path('processos/', include('apps.processos.urls')),
    path(
        'login/',
        auth_views.LoginView.as_view(template_name='registration/login.html'),
        name='login',
    ),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('api/v1/', include('apps.processos.api_urls')),
    path('api-auth/', include('rest_framework.urls')),
]
