# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Carro',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('Placa', models.CharField(default='xxx-xxxx', max_length=20)),
                ('Renava', models.CharField(max_length=20)),
                ('Marca', models.CharField(max_length=20)),
                ('Modelo', models.CharField(max_length=20)),
                ('Ano', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Carro',
                'verbose_name_plural': 'Carros',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Esposa',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('Nome', models.CharField(max_length=20)),
                ('Casamento_Data', models.DateField(verbose_name='Certidao_de_Casamento')),
                ('Cpf', models.CharField(unique=True, verbose_name='CPF', max_length=11)),
                ('Rg', models.CharField(max_length=20)),
                ('Data_de_Exp', models.DateField(verbose_name='Data_de_Exp')),
                ('Titulo_Eleitor', models.CharField(max_length=20)),
                ('Passaporte', models.CharField(max_length=20, blank=True)),
                ('Nacionalidade', models.CharField(max_length=20, blank=True)),
                ('Naturalidade', models.CharField(max_length=20, blank=True)),
                ('Formacao', models.CharField(max_length=20, blank=True)),
                ('Proficao', models.CharField(max_length=20)),
                ('Indioma', models.CharField(max_length=10, blank=True)),
                ('Tempo_de_Evangelho', models.CharField(max_length=10, blank=True)),
            ],
            options={
                'verbose_name': 'Esposa',
                'verbose_name_plural': 'Esposas',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Filho',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('Nome', models.CharField(max_length=30)),
                ('Data_de_Nascimento', models.DateField(verbose_name='Data_de_Nascimento')),
            ],
            options={
                'verbose_name': 'Filho',
                'verbose_name_plural': 'Filhos',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Igreja',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('IURD', models.CharField(blank=True, choices=[('barao', 'BARAO'), ('lorival', 'LORIVAL'), ('sede', 's')], max_length=10)),
                ('CNPJ', models.CharField(max_length=15, blank=True)),
                ('Contato', models.CharField(max_length=15, blank=True)),
                ('Endereco', models.CharField(max_length=15, blank=True)),
                ('Numero', models.CharField(max_length=15)),
                ('Bairro', models.CharField(max_length=15, blank=True)),
                ('Cidade', models.CharField(max_length=15, blank=True)),
                ('Cep', models.CharField(max_length=15, blank=True)),
                ('Telefone', models.CharField(max_length=15, blank=True)),
                ('Email', models.CharField(max_length=15, blank=True)),
                ('Possui_Carro', models.BooleanField(default=True)),
                ('Carro', models.ForeignKey(to='core.Carro')),
            ],
            options={
                'verbose_name': 'Igreja',
                'verbose_name_plural': 'Igrejas',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Pastor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('Nome', models.CharField(max_length=30)),
                ('estado_civil', models.CharField(choices=[('C', 'CASADO'), ('D', 'DIRVOCIADO'), ('S', 'SOLTEIRO'), ('V', 'VIUVO')], max_length=10)),
                ('Pastor_Regional', models.BooleanField(default=False)),
                ('Data_de_Nascimento', models.DateField(verbose_name='Data_de_Nascimento')),
                ('Cpf', models.CharField(max_length=20, blank=True)),
                ('Rg', models.CharField(max_length=20)),
                ('Data_de_Exp', models.DateField(verbose_name='Data_de_Exp')),
                ('Cnh', models.CharField(max_length=20)),
                ('Regiao', models.CharField(choices=[('barao', 'BARAO'), ('lorival', 'LORIVAL'), ('sede', 's')], max_length=10)),
                ('Titulo_Eleitor', models.CharField(max_length=20)),
                ('Zona', models.CharField(max_length=10)),
                ('Seção', models.CharField(max_length=20)),
                ('Passaporte', models.CharField(max_length=15)),
                ('Nacionalidade', models.CharField(max_length=20, blank=True)),
                ('Naturalidada_UF', models.CharField(max_length=20, blank=True)),
                ('Grau_de_Instrução', models.CharField(blank=True, choices=[('1°', '1°Grau'), ('2°', '2°Grau'), ('S', 'Superior')], max_length=30)),
                ('Proficao', models.CharField(max_length=20, blank=True)),
                ('Indioma', models.CharField(max_length=10)),
                ('Telefone', models.CharField(max_length=10)),
                ('Celula', models.CharField(default='', max_length=20)),
                ('Email', models.EmailField(unique=True, max_length=75)),
                ('Whatsapp', models.CharField(max_length=10, blank=True)),
                ('Pastor', models.CharField(blank=True, choices=[('Aux', 'Auxiliar'), ('Pr', 'Pr.Titular'), ('Bp', ' Bispo')], max_length=20)),
                ('Esposa', models.ForeignKey(to='core.Esposa')),
            ],
            options={
                'verbose_name': 'Pastor',
                'verbose_name_plural': 'Pastores',
            },
            bases=(models.Model,),
        ),
    ]
