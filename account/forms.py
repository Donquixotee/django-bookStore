from django import forms
from .models import UserBase


class RegistrationForm(forms.ModelForm):
    user_name = forms.CharField(label='Enter Username', min_length=4, max_length=50, help_text='Required')
    email = forms.EmailField(max_length=100, help_text='Required', error_messages={'required': 'Sorry, you will need an email'})
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput)

    class Meta:
        model = UserBase
        fields = ('user_name', 'email',)

    def clean_username(self):
        user_name = self.cleaned_data['user_name'].lower()
        occurrence = UserBase.objects.filter(user_name=user_name)
        if occurrence.count():
            raise forms.ValidationError("Username already exist")
        
        return user_name

    def clean_password2(self):
        pswrd = self.cleaned_data
        if pswrd['password'] !=pswrd['password2']:
            raise forms.ValidationError("password doent match")

        return pswrd['password2']

    def clean_email(self):
        email = self.cleaned_data['email']
        occurrence = UserBase.objects.filter(email=email)
        if occurrence.exists():
            raise forms.ValidationError("email already exist")
        
        return email
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['user_name'].widget.attrs.update(
            {'class': 'form-control mb-3', 'placeholder': 'Username'})
        self.fields['email'].widget.attrs.update(
            {'class': 'form-control mb-3', 'placeholder': 'E-mail', 'name': 'email', 'id': 'id_email'})
        self.fields['password'].widget.attrs.update(
            {'class': 'form-control mb-3', 'placeholder': 'Password'})
        self.fields['password2'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Repeat Password'})