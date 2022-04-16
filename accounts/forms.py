from django import forms
from django.contrib.auth.models import User

#Есть два вида форм
# 1) ModelForm -  Формы основанные на полях модели
# 2) Form - Обычная форма.

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(
        attrs={"class":"form-control"}
        ))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={"class":"form-control"}
    ))



class UserRegisterForm(forms.ModelForm):
    password = forms.CharField(
        label='Пароль',
        widget=forms.PasswordInput(attrs={"class":"form-control"}))
    password2 = forms.CharField(
        label='Повторите пароль', 
        widget=forms.PasswordInput(attrs={"class":"form-control"})
        )

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')
        widgets = {
            "username": forms.TextInput(attrs={"class":"form-control"}),
            "first_name": forms.TextInput(attrs={"class":"form-control"}),
            "last_name": forms.TextInput(attrs={"class":"form-control"}),
            "email": forms.EmailInput(attrs={"class":"form-control"}),
        }
    
    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Пароли не совпадают')
        return cd['password2']