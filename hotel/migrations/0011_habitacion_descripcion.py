# Generated by Django 2.1.5 on 2020-08-12 23:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0010_auto_20200812_1812'),
    ]

    operations = [
        migrations.AddField(
            model_name='habitacion',
            name='descripcion',
            field=models.CharField(default='esta habitacion es la mas hermosa de todas', max_length=100),
            preserve_default=False,
        ),
    ]
