# Generated by Django 2.0.5 on 2019-04-21 23:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cric', '0012_auto_20190421_1842'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='guest_team_score',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='match',
            name='home_team_score',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='squad_position',
            field=models.CharField(choices=[('batsman', 'Batsman'), ('long', 'Long_off'), ('midfielder', 'Mid_on'), ('midfielder', 'Mid_off'), ('wicketKeeper', 'Wicket_Keeper'), ('bowler', 'Bowler'), ('long', 'Long_on'), ('gullypoint', 'Gully_point'), ('none', 'None'), ('slip', 'Slip'), ('allrounder', 'All_rounder')], default='none', max_length=20),
        ),
    ]