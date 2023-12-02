# Generated by Django 4.2.4 on 2023-12-02 14:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_rename_data_inicio_jogo_data_hora_inicio_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Estatistica',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vitorias', models.IntegerField(default=0, verbose_name='Vitorias')),
                ('derrotas', models.IntegerField(default=0, verbose_name='Derrotas')),
                ('empates', models.IntegerField(default=0, verbose_name='Empates')),
                ('gols_marcados', models.IntegerField(default=0, verbose_name='Gols Marcados')),
                ('gols_sofridos', models.IntegerField(default=0, verbose_name='Gols Sofridos')),
                ('cartao_amarelo', models.IntegerField(default=0, verbose_name='Cartão Amarelo')),
                ('cartao_vermelho', models.IntegerField(default=0, verbose_name='Cartão Vermelho')),
                ('saldo_gols', models.IntegerField(default=0, verbose_name='Saldo de Gols')),
                ('pontuacao', models.IntegerField(default=0, verbose_name='Pontuação')),
                ('time', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='estatistica_time', to='core.time', verbose_name='Time')),
                ('torneio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='estatistica_torneio', to='core.torneio', verbose_name='Torneio')),
            ],
            options={
                'verbose_name': 'Estatistica',
                'verbose_name_plural': 'Estatisticas',
            },
        ),
        migrations.DeleteModel(
            name='CompetidoPor',
        ),
    ]
