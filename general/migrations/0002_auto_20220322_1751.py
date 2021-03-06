# Generated by Django 3.2.8 on 2022-03-22 23:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='general',
            name='efectivo_caja',
            field=models.DecimalField(decimal_places=2, default=None, max_digits=9),
        ),
        migrations.AlterField(
            model_name='general',
            name='ingreso_tarjeta',
            field=models.DecimalField(decimal_places=2, default=None, max_digits=9),
        ),
        migrations.AlterField(
            model_name='general',
            name='numero_mesas',
            field=models.IntegerField(default=None),
        ),
        migrations.AlterField(
            model_name='general',
            name='propina_tarjeta',
            field=models.DecimalField(decimal_places=2, default=None, max_digits=9),
        ),
    ]
