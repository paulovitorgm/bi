from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import include, path, reverse_lazy

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
    path(
        'recuperar-senha/',
        auth_views.PasswordResetView.as_view(
            template_name='registration/password_reset_form.html',
            email_template_name='registration/password_reset_email.html',
            subject_template_name='registration/password_reset_subject.txt',
            success_url=reverse_lazy('password_reset_done'),
        ),
        name='password_reset',
    ),
    path(
        'recuperar-senha/enviado/',
        auth_views.PasswordResetDoneView.as_view(
            template_name='registration/password_reset_done.html',
        ),
        name='password_reset_done',
    ),
    path(
        'recuperar-senha/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(
            template_name='registration/password_reset_confirm.html',
            success_url=reverse_lazy('password_reset_complete'),
        ),
        name='password_reset_confirm',
    ),
    path(
        'recuperar-senha/concluido/',
        auth_views.PasswordResetCompleteView.as_view(
            template_name='registration/password_reset_complete.html',
        ),
        name='password_reset_complete',
    ),
    path('api/v1/', include('apps.processos.api_urls')),
    path('api-auth/', include('rest_framework.urls')),
]
