# Generated by Django 5.1.1 on 2025-02-08 17:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Etudiants', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('corps', models.TextField(max_length='300', verbose_name='message')),
                ('sendEtudiantt', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Etudiants.etudiant', verbose_name='Envoie Etudiant')),
            ],
        ),
    ]
