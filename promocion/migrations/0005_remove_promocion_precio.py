# Generated by Django 3.2.8 on 2022-03-14 14:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('promocion', '0004_productosdias_precio_descuento'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='promocion',
            name='precio',
        ),
    ]
