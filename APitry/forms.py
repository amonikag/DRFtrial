from django.contrib.auth.models import User
from django import forms

class UserForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput)
    name=forms.CharField()
    phone_no=forms.IntegerField()
    class Meta:
        model=User
        fields=['name','username','email','phone_no','password']