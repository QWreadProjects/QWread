from django.contrib.auth.forms import UserCreationForm

from users.models import User


# from django import forms


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'sex', 'email', 'phone', 'head_img']
