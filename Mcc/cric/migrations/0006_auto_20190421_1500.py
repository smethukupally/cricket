# Generated by Django 2.0.5 on 2019-04-21 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cric', '0005_auto_20190421_1458'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='squad_position',
            field=models.CharField(choices=[('batsman', 'Batsman'), ('gullypoint', 'Gully_point'), ('midfielder', 'Mid_off'), ('midfielder', 'Mid_on'), ('wicketKeeper', 'Wicket_Keeper'), ('long', 'Long_off'), ('allrounder', 'All_rounder'), ('long', 'Long_on'), ('none', 'None'), ('slip', 'Slip'), ('bowler', 'Bowler')], default='none', max_length=20),
        ),
    ]
