# Generated by Django 4.1.7 on 2023-04-18 12:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0007_projetoavaliado'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='enviarprojeto',
            name='nota',
        ),
    ]
