from django import forms

class EleveForm(forms.Form):
    name = forms.CharField(label='Name', max_length=100)
    last_name = forms.CharField(label='Last_name', max_length=100)
    sex = forms.ChoiceField(label='Sex', choices=[('M', 'Masculin'), ('F', 'Féminin')])
    registration = forms.CharField(label='Registration', max_length=10)
    date_birth = forms.DateField(label='Date_birth')
    classe = forms.CharField(label='Classe', max_length=50)
    phone = forms.CharField(label='Phone', max_length=15)
    city = forms.CharField(label='City', max_length=15)



 