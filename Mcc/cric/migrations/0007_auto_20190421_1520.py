# Generated by Django 2.0.5 on 2019-04-21 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cric', '0006_auto_20190421_1500'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='squad_position',
            field=models.CharField(choices=[('none', 'None'), ('midfielder', 'Mid_on'), ('allrounder', 'All_rounder'), ('gullypoint', 'Gully_point'), ('midfielder', 'Mid_off'), ('bowler', 'Bowler'), ('long', 'Long_on'), ('wicketKeeper', 'Wicket_Keeper'), ('long', 'Long_off'), ('batsman', 'Batsman'), ('slip', 'Slip')], default='none', max_length=20),
        ),
    ]
