from django import forms
from django.contrib.auth.forms import AuthenticationForm
from app.models import MyUser


class MyUserAuthenticationForm(AuthenticationForm):
    class Meta:
        model = MyUser
        fields = ('username', 'age')


class FeedbackForm(forms.Form):
    name = forms.CharField()
    text = forms.CharField(widget=forms.Textarea)




