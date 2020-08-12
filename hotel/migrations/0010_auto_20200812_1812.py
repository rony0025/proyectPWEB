# Generated by Django 2.1.5 on 2020-08-12 23:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0009_auto_20200801_2132'),
    ]

    operations = [
        migrations.AddField(
            model_name='habitacion',
            name='mantenimineto',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='habitacion',
            name='tipo',
            field=models.CharField(choices=[('SENCILLA', 'Sencilla'), ('DOBLE', 'Doble'), ('MATRIMONIAL', 'Matrimonial'), ('SUITE', 'Suite')], default='SENCILLA', max_length=15),
        ),
    ]