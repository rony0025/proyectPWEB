# Generated by Django 2.1.5 on 2020-08-12 23:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0012_habitacion_mantenimiento'),
    ]

    operations = [
        migrations.AddField(
            model_name='habitacion',
            name='descripcion',
            field=models.CharField(default='Esta es una habitacion', max_length=100),
            preserve_default=False,
        ),
    ]