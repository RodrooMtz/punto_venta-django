# Generated by Django 3.2.8 on 2022-03-22 15:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('carta', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductosDias',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('producto1', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='carta.productomenu')),
            ],
        ),
        migrations.CreateModel(
            name='Promocion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_promocion', models.CharField(max_length=200, unique=True)),
                ('imagen', models.ImageField(blank=True, upload_to='photos/promo')),
                ('precio', models.IntegerField(blank=True, default=0)),
                ('dia', models.CharField(choices=[('Lunes', 'Lunes'), ('Martes', 'Martes'), ('Miércoles', 'Miércoles'), ('Jueves', 'Jueves'), ('Viernes', 'Viernes'), ('Sábado', 'Sábado'), ('Domingo', 'Domingo')], default='', max_length=10)),
                ('producto', models.ManyToManyField(blank=True, through='promocion.ProductosDias', to='carta.ProductoMenu')),
            ],
        ),
        migrations.AddField(
            model_name='productosdias',
            name='promocion1',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='promocion.promocion'),
        ),
    ]
