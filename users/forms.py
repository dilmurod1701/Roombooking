from django.contrib.auth.forms import UserChangeForm, UserCreationForm

from .models import User


class FormUserChange(UserChangeForm):
    class Meta:
        model = User
        fields = '__all__'


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = '__all__'
