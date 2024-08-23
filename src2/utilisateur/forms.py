from django import forms

class UsersForm(forms.Form):
    users = forms.CharField(label='Users', max_length=50)
    password = forms.CharField(label='Password', max_length=50)
  
   

