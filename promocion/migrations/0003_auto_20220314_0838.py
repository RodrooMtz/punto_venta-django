# Generated by Django 3.2.8 on 2022-03-14 14:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('carta', '0001_initial'),
        ('promocion', '0002_auto_20220311_1743'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productosdias',
            name='producto1',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='carta.productomenu'),
        ),
        migrations.AlterField(
            model_name='productosdias',
            name='promocion1',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='promocion.promocion'),
        ),
        migrations.AlterField(
            model_name='promocion',
            name='producto',
            field=models.ManyToManyField(blank=True, through='promocion.ProductosDias', to='carta.ProductoMenu'),
        ),
    ]
