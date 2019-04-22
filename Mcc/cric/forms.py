from django import forms
from .models import Team, Score, Player, MCCrole, Match
from django.forms.utils import ValidationError
from django.contrib.auth import authenticate, get_user_model, login, logout
from django.core.exceptions import ObjectDoesNotExist
import re

class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ('team_name', 'team_logo_url', 'school','active_status','coach')

class ScoreForm(forms.ModelForm):
    class Meta:
        model = Score
        fields = ('player', 'score','wickets')

    def __init__(self, *args, **kwargs):
        team_id=kwargs.pop('team_id')
        super(ScoreForm, self).__init__(*args, **kwargs)
        self.fields['player'].queryset = Player.objects.filter(team__id=team_id)

class MatchForm(forms.ModelForm):
    class Meta:
        model = Match
        fields = ('home_team', 'guest_team', 'match_day', 'match_start_time', 'match_end_time',
                  'field', 'match_referee', 'match_status','home_team_score','guest_team_score', 'referee_comments')

class MatchStatusForm(forms.ModelForm):
    class Meta:
        model = Match
        fields = ('match_status', 'referee_comments')

class PlayerForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = ('first_name', 'last_name','email','phone','team','eligibility_status','team_role', 'squad_position', 'street', 'city','state','zipcode')


class AssignRoleForm(forms.ModelForm):
    class Meta:
        model = MCCrole
        fields = ['role', 'receiver_name', 'receiver_email']

    def clean(self):
        receiver_email = self.cleaned_data['receiver_email']
        try:
           mccrole = MCCrole.objects.filter(receiver_email=receiver_email).order_by('receiver_name').first()
           print('mccrole--', mccrole)
        except ObjectDoesNotExist:
            return receiver_email
        if mccrole:
            raise forms.ValidationError('Email is already taken and assigned to '+mccrole.role+'')





User = get_user_model()


class PasswordResetRequestForm(forms.Form):
    email_or_username = forms.CharField(label=("Email Or Username"), max_length=254)


class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError("This user does not exist")
            if not user.check_password(password):
                raise forms.ValidationError("Incorrect Password")
            if not user.is_active:
                raise forms.ValidationError("This user is no longer active")
        return super(UserLoginForm, self).clean(*args, **kwargs)


class UserRegisterForm(forms.ModelForm):
    username = forms.CharField(label='Username', max_length=30)
    email = forms.EmailField(label='Email')
    password = forms.CharField(label='Password', widget=forms.PasswordInput())
    password1 = forms.CharField(label='Password (Again)', widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    # password validation
    def clean_password2(self):
        if 'password' in self.cleaned_data:
            password1 = self.cleaned_data['password']
            password2 = self.cleaned_data['password1']
            if password1 == password2:
                return password2
        raise forms.ValidationError('Passwords do not match.')

    def clean_username(self):
        username = self.cleaned_data['username']
        if not re.search(r'^\w+$', username):
            raise forms.ValidationError('Username can only contain alphanumeric characters and the underscore.')
        try:
            User.objects.get(username=username)
        except ObjectDoesNotExist:
            return username
        raise forms.ValidationError('Username is already taken.')

    def clean(self, *args, **kwargs):
        email = self.cleaned_data.get('email')

        try:
            mccrole = MCCrole.objects.get(receiver_email=email)
        except ObjectDoesNotExist:
            mccrole = None

        print('mccrole--', mccrole)
        if mccrole is not None:
            try:
                email_qs = User.objects.get(email=email)
            except ObjectDoesNotExist:
                email_qs = None

            print('email_qs--', email_qs)
            if email_qs is not None:
                print('email_qs 123--', email_qs)
                usergroup = email_qs.groups.all()
                groupname = ''
                if usergroup:
                    for name in usergroup:
                        groupname = name
                    print("groupname---",groupname)
                raise forms.ValidationError("This email has already been registered as '"+ str(groupname) +"'")
        else:
            raise forms.ValidationError("You are not authorized to register, please contact MCC administration'")
        return super(UserRegisterForm, self).clean(*args, **kwargs)
