# Generated by Django 5.1.4 on 2024-12-10 18:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('senhas', '0002_fila_senha_fila'),
    ]

    operations = [
        migrations.AlterField(
            model_name='senha',
            name='fila',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='senhas.fila'),
        ),
    ]