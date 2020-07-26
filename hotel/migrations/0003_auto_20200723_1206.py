# Generated by Django 2.1.5 on 2020-07-23 17:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0002_auto_20200723_0955'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cliente',
            name='habitacion',
        ),
        migrations.AddField(
            model_name='habitacion',
            name='cliente',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='hotel.Cliente'),
            preserve_default=False,
        ),
    ]