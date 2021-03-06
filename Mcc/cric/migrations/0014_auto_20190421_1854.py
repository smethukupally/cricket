# Generated by Django 2.0.5 on 2019-04-21 23:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cric', '0013_auto_20190421_1852'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='match_status',
            field=models.CharField(choices=[('scheduled', 'Scheduled'), ('in_progress', 'In Progress'), ('finished', 'finished'), ('cancelled', 'Cancelled'), ('abandoned', 'Abandoned')], default='scheduled', max_length=20),
        ),
        migrations.AlterField(
            model_name='player',
            name='squad_position',
            field=models.CharField(choices=[('midfielder', 'Mid_on'), ('wicketKeeper', 'Wicket_Keeper'), ('long', 'Long_off'), ('slip', 'Slip'), ('midfielder', 'Mid_off'), ('gullypoint', 'Gully_point'), ('long', 'Long_on'), ('allrounder', 'All_rounder'), ('bowler', 'Bowler'), ('batsman', 'Batsman'), ('none', 'None')], default='none', max_length=20),
        ),
    ]
