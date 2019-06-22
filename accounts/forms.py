from django import forms
from django.contrib.auth.models import User
from accounts.models import Profile
from django.contrib.auth.forms import UserCreationForm

def unique_email(email):
    users = User.objects.all()
    if users.filter(email=email).exists():
        raise forms.ValidationError("A user with this email already exists.")

class UserForm(UserCreationForm):
    # password = forms.CharField(widget=forms.PasswordInput())
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(required = True, validators=[unique_email])
    # confirm_password=forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = (
        'first_name',
        'last_name',
        'email',
        'username',
        'password1',
        'password2'
        )

class EditUserForm(forms.ModelForm):
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(required = True)
    class Meta():
        model = User
        fields = ('first_name', 'last_name', 'email')

class EditProfileForm(forms.ModelForm):
    class Meta():
        model = Profile
        exclude = ('user',)