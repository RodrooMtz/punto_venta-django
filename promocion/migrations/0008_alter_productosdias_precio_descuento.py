# Generated by Django 3.2.8 on 2022-03-15 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('promocion', '0007_alter_promocion_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productosdias',
            name='precio_descuento',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
