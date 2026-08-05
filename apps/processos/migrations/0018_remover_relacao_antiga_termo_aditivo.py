import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [('processos', '0017_termo_aditivo_pertence_ao_processo')]

    operations = [
        migrations.RemoveField(model_name='processoprojeto', name='termo_adtivo'),
        migrations.AlterField(
            model_name='termosadtivos',
            name='processo',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name='termos_aditivos',
                to='processos.processoprojeto',
            ),
        ),
    ]
