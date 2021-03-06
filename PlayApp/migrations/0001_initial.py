# Generated by Django 4.0 on 2022-01-16 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.EmailField(max_length=40)),
                ('comentario', models.TextField(max_length=300)),
                ('fecha', models.DateTimeField(auto_now=True, max_length=12)),
            ],
        ),
        migrations.CreateModel(
            name='Publicacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50)),
                ('nombre', models.EmailField(max_length=40)),
                ('noticia', models.TextField(max_length=5000)),
                ('fecha', models.DateTimeField(auto_now=True, max_length=12)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('email', models.EmailField(max_length=254)),
                ('clave', models.CharField(max_length=12)),
                ('tipo', models.CharField(default='', max_length=6)),
            ],
        ),
    ]
