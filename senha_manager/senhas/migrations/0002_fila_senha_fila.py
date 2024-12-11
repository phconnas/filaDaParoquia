# Generated by Django 5.1.4 on 2024-12-10 18:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('senhas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fila',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('id_usb', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='senha',
            name='fila',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='senhas.fila'),
            preserve_default=False,
        ),
    ]
