# Generated by Django 4.0 on 2022-01-18 23:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PlayApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comentario',
            name='publicacion',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='publicacion',
            name='nombre',
            field=models.CharField(max_length=40),
        ),
    ]
