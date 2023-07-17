from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUser


class CustomUserCreation(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'username', 'age', 'email',)


class CustomUserChange(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'username', 'age', 'email',)
