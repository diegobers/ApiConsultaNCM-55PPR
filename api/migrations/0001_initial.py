# Generated by Django 4.0.1 on 2022-02-22 20:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CommonMercosulNomenclature',
            fields=[
                ('Codigo', models.CharField(blank=True, max_length=10, primary_key=True, serialize=False)),
                ('Descricao', models.CharField(max_length=5000)),
                ('Data_Inicio', models.CharField(max_length=255)),
                ('Data_Fim', models.CharField(max_length=255)),
                ('Tipo_Ato', models.CharField(max_length=255)),
                ('Numero_Ato', models.CharField(max_length=255)),
                ('Ano_Ato', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ArquivoJSON',
            fields=[
                ('Data_Ultima_Atualizacao_NCM', models.CharField(blank=True, max_length=255, primary_key=True, serialize=False)),
                ('Nomenclaturas', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='api.commonmercosulnomenclature')),
            ],
        ),
    ]
