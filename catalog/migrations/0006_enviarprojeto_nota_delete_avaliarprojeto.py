# Generated by Django 4.1.7 on 2023-04-13 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_alter_enviarprojeto_dataenvio_remove_premio_autor_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='enviarprojeto',
            name='nota',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='AvaliarProjeto',
        ),
    ]