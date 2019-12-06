from django import forms
from .models import *


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('teamName', 'teamId', 'nameT1', 'nameT2', 'schoolName')
        # labels = {'Enter your School Name:' : 'schoolName',
        #           " Enter your Team Name ": 'teamName',
        #           "Whats your Team Id": 'teamId',
        #           "Student 1 Name": 'nameT1',
        #             "Student2 Name": 'nameT2'}


class QuizForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ('A', 'B', 'C', 'D', 'question')


class AForm(forms.Form):
    CHOICES = [
        ('one', '2'),
        ('two', '3')
    ]
    like = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)
