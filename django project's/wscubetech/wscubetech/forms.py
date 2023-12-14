from django import forms

class usersForm(forms.Form):
    num1=forms.CharField(label="Value 1:",required=False,widget=forms.TextInput(attrs={'class': "form-control"}))
    num2=forms.CharField(label="Value 2:",required=False,widget=forms.TextInput(attrs={'class': "form-control"}))
    num3=forms.CharField(label="Value 3:",required=False,widget=forms.TextInput(attrs={'class': "form-control"}))
    email = forms.EmailField()