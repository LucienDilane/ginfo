# Generated by Django 5.1.1 on 2025-02-10 02:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Echange', '0003_remove_messagerecu_receiveetudiantt_and_more'),
        ('Etudiants', '0003_etudiant_avatar_etudiant_statut'),
        ('Groupe', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='media',
            field=models.CharField(default=0, max_length=255, verbose_name='mediaIb'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='message',
            name='date_envoie',
            field=models.DateTimeField(auto_now_add=True, verbose_name='dateEnvoie'),
        ),
        migrations.CreateModel(
            name='Publication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(max_length=300, verbose_name='contenu')),
                ('media', models.CharField(max_length=255, verbose_name='mediaGroup')),
                ('date_pub', models.DateTimeField(auto_now_add=True, verbose_name='datePub')),
                ('auteur', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='auteur', to='Etudiants.etudiant')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pubGroup', to='Groupe.group')),
            ],
        ),
        migrations.CreateModel(
            name='Commentaire',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(max_length=300, verbose_name='commentaire')),
                ('media', models.CharField(max_length=255, verbose_name='mediaComm')),
                ('date_com', models.DateTimeField(auto_now_add=True, verbose_name='dateComm')),
                ('auteur', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Etudiants.etudiant')),
                ('publication', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Echange.publication')),
            ],
        ),
    ]
