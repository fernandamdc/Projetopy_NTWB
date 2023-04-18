# Generated by Django 4.1.7 on 2023-04-13 23:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0006_enviarprojeto_nota_delete_avaliarprojeto'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjetoAvaliado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nota', models.DecimalField(decimal_places=False, max_digits=2)),
                ('avaliador', models.ManyToManyField(to='catalog.avaliador')),
                ('projeto', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='catalog.enviarprojeto')),
            ],
        ),
    ]