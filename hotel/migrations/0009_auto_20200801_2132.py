# Generated by Django 2.1.5 on 2020-08-02 02:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0008_habitacion_estado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='habitacion',
            name='dias',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='habitacion',
            name='servicios',
            field=models.PositiveIntegerField(null=True),
        ),
    ]