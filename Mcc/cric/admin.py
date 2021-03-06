from django.contrib import admin
from .models import School, Field, Team, Match, Player, Score, MCCrole, Score


# Register your models here.


class SchoolList(admin.ModelAdmin):
    list_display = ('school_name', 'city', 'state',)
    list_filter = ('city', 'state',)
    search_fields = ('school_name',)
    ordering = ['school_name']


class FieldList(admin.ModelAdmin):
    list_display = ('field_name', 'city', 'state')
    list_filter = ('city', 'state')
    search_fields = ('field_name',)
    ordering = ['field_name']


class TeamList(admin.ModelAdmin):
    list_display = ('team_name', 'school')
    search_fields = ('team_name',)
    ordering = ['team_name']


class MatchList(admin.ModelAdmin):
    list_display = ('match_day', 'home_team', 'guest_team')
    list_filter = ('home_team', 'guest_team', 'match_status')
    search_fields = ('home_team',)
    ordering = ['-match_day']


class PlayerList(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'team')
    list_filter = ('team', 'eligibility_status')
    search_fields = ('first_name', 'last_name')
    ordering = ['first_name']


class ScoreList(admin.ModelAdmin):
    list_display = ('player', 'team', 'match')
    list_filter = ('team', 'player')
    search_fields = ('team', 'player')
    ordering = ['-created_date']


class MCCroleList(admin.ModelAdmin):
    list_display = ('role', 'receiver_name', 'receiver_email')
    list_filter = ('role', 'receiver_name')
    search_fields = ('role', 'receiver_name')
    ordering = ['-role']


admin.site.register(School, SchoolList)
admin.site.register(Field, FieldList)
admin.site.register(Team)
admin.site.register(Match, MatchList)
admin.site.register(Player, PlayerList)
admin.site.register(Score, ScoreList)
admin.site.register(MCCrole, MCCroleList)
