# Generated by Django 4.2.4 on 2023-12-02 14:25

import core.models.cartao
import core.models.gol
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_alter_cartao_tempo_alter_gol_tempo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartao',
            name='tempo',
            field=models.CharField(max_length=6, validators=[core.models.cartao.validate_custom_time_format], verbose_name='Tempo em que registrou'),
        ),
        migrations.AlterField(
            model_name='gol',
            name='tempo',
            field=models.CharField(max_length=6, validators=[core.models.gol.validate_custom_time_format], verbose_name='Tempo em que registrou'),
        ),
    ]