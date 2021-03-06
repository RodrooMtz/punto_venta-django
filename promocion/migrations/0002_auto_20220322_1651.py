# Generated by Django 3.2.8 on 2022-03-22 22:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carta', '0001_initial'),
        ('promocion', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='promocion',
            name='dia',
            field=models.CharField(choices=[('Lunes', 'Lunes'), ('Martes', 'Martes'), ('Miércoles', 'Miércoles'), ('Jueves', 'Jueves'), ('Viernes', 'Viernes'), ('Sábado', 'Sábado'), ('Domingo', 'Domingo')], default=None, max_length=10),
        ),
        migrations.AlterField(
            model_name='promocion',
            name='imagen',
            field=models.ImageField(upload_to='photos/promo'),
        ),
        migrations.AlterField(
            model_name='promocion',
            name='precio',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='promocion',
            name='producto',
            field=models.ManyToManyField(through='promocion.ProductosDias', to='carta.ProductoMenu'),
        ),
    ]
