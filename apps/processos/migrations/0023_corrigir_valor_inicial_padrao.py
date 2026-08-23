from decimal import Decimal

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [('processos', '0022_alter_processoprojeto_ods_onu')]

    operations = [
        migrations.AlterField(
            model_name='processoprojeto',
            name='valor_inicial',
            field=models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=25),
        ),
    ]
