from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


def audit_fields(model_name):
    return [
        migrations.AddField(
            model_name=model_name,
            name='criado_em',
            field=models.DateTimeField(
                auto_now_add=True, db_index=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name=model_name,
            name='atualizado_em',
            field=models.DateTimeField(auto_now=True, db_index=True),
        ),
        migrations.AddField(
            model_name=model_name,
            name='origem_registro',
            field=models.CharField(
                choices=[
                    ('manual', 'Cadastro manual'),
                    ('importacao', 'Importação'),
                    ('integracao', 'Integração'),
                ],
                default='manual',
                max_length=20,
            ),
        ),
        migrations.AddField(
            model_name=model_name,
            name='criado_por',
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name=f'processos_{model_name}_criados',
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name=model_name,
            name='atualizado_por',
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name=f'processos_{model_name}_atualizados',
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]


class Migration(migrations.Migration):
    dependencies = [
        ('processos', '0014_termosadtivos_remove_processoprojeto_forma_aprovacao_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        operation
        for model_name in [
            'abrangencia',
            'entidadeparceira',
            'itemplanodespesa',
            'modalidade',
            'natureza',
            'participesmodel',
            'processoprojeto',
            'termosadtivos',
            'tipodespesa',
            'unidade',
        ]
        for operation in audit_fields(model_name)
    ]
