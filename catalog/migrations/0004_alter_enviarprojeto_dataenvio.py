# Generated by Django 4.1.7 on 2023-04-13 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_auto_20230410_1045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enviarprojeto',
            name='dataEnvio',
            field=models.DateField(auto_created=True),
        ),
    ]
