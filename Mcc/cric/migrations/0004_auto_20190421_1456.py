# Generated by Django 2.0.5 on 2019-04-21 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cric', '0003_auto_20190421_1421'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='squad_position',
            field=models.CharField(choices=[('bowler', 'Bowler'), ('long', 'Long_off'), ('batsman', 'Batsman'), ('midfielder', 'Mid_off'), ('allrounder', 'All_rounder'), ('long', 'Long_on'), ('slip', 'Slip'), ('none', 'None'), ('midfielder', 'Mid_on'), ('wicketKeeper', 'Wicket_Keeper'), ('gullypoint', 'Gully_point')], default='none', max_length=20),
        ),
    ]
