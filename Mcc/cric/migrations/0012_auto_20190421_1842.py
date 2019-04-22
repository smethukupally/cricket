# Generated by Django 2.0.5 on 2019-04-21 23:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cric', '0011_auto_20190421_1658'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='squad_position',
            field=models.CharField(choices=[('midfielder', 'Mid_off'), ('batsman', 'Batsman'), ('long', 'Long_on'), ('long', 'Long_off'), ('none', 'None'), ('wicketKeeper', 'Wicket_Keeper'), ('bowler', 'Bowler'), ('allrounder', 'All_rounder'), ('slip', 'Slip'), ('gullypoint', 'Gully_point'), ('midfielder', 'Mid_on')], default='none', max_length=20),
        ),
    ]
