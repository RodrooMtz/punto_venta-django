# Generated by Django 3.2.8 on 2022-03-22 22:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('promocion', '0002_auto_20220322_1651'),
    ]

    operations = [
        migrations.AlterField(
            model_name='promocion',
            name='dia',
            field=models.CharField(choices=[('Lunes', 'Lunes'), ('Martes', 'Martes'), ('Miércoles', 'Miércoles'), ('Jueves', 'Jueves'), ('Viernes', 'Viernes'), ('Sábado', 'Sábado'), ('Domingo', 'Domingo')], max_length=10),
        ),
        migrations.AlterField(
            model_name='promocion',
            name='precio',
            field=models.IntegerField(default=None),
        ),
    ]