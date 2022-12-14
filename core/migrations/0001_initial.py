# Generated by Django 4.1.2 on 2022-11-19 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('tipo', models.CharField(choices=[('lacto', 'LACTICIO'), ('prot', 'PROTEINA'), ('hort', 'HORTALICAS')], max_length=20)),
                ('codigo', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Servico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('tipo', models.CharField(choices=[('instal', 'INSTALAÇAO'), ('mont', 'MONTAGEM'), ('manut', 'MANUTENÇAO')], max_length=20)),
                ('codigo', models.IntegerField()),
            ],
        ),
    ]
