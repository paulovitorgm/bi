import django.db.models.deletion
from django.db import migrations, models


def vincular_termos_a_processos(apps, schema_editor):
    Processo = apps.get_model('processos', 'ProcessoProjeto')
    Termo = apps.get_model('processos', 'TermosAdtivos')

    for processo in Processo.objects.all():
        for termo in processo.termo_adtivo.all():
            if termo.processo_id is None:
                termo.processo_id = processo.pk
                termo.save(update_fields=['processo'])
            else:
                Termo.objects.create(
                    processo_id=processo.pk,
                    termo=f'{termo.termo[:80]} ({processo.pk})',
                    dt_assinatura=termo.dt_assinatura,
                    dt_termino=termo.dt_termino,
                    valor=termo.valor,
                )

    Termo.objects.filter(processo__isnull=True).delete()


class Migration(migrations.Migration):
    atomic = False
    dependencies = [('processos', '0016_alter_abrangencia_atualizado_por_and_more')]

    operations = [
        migrations.AddField(
            model_name='termosadtivos',
            name='processo',
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name='termos_aditivos',
                to='processos.processoprojeto',
            ),
        ),
        migrations.RunPython(vincular_termos_a_processos, migrations.RunPython.noop),
    ]
