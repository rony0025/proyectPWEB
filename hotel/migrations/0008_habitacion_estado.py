# Generated by Django 2.1.5 on 2020-08-02 02:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0007_auto_20200801_2110'),
    ]

    operations = [
        migrations.AddField(
            model_name='habitacion',
            name='estado',
            field=models.BooleanField(default=False),
        ),
    ]