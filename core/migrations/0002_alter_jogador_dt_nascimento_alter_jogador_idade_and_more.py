# Generated by Django 4.2.4 on 2023-10-19 00:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jogador',
            name='dt_nascimento',
            field=models.DateField(verbose_name='Data de nascimento'),
        ),
        migrations.AlterField(
            model_name='jogador',
            name='idade',
            field=models.IntegerField(blank=True, null=True, verbose_name='Idade'),
        ),
        migrations.AlterField(
            model_name='jogo',
            name='torneio',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='torneio_jogo', to='core.torneio', verbose_name='Torneio'),
        ),
    ]
