from django.forms import ModelForm
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.core.exceptions import ValidationError

UserModel = get_user_model()


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = UserModel
        fields = ('email', 'username', 'is_freelancer',
                  'first_name', 'last_name')

    def clean_email(self):
        email = self.cleaned_data['email']
        User = get_user_model()
        if User.objects.filter(email=email).exists():
            raise ValidationError("Такой E-mail уже существует!")
        return email


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = UserModel
        fields = ('email', 'first_name', 'last_name', 'experience')


class ProfileForm(ModelForm):
    class Meta:
        model = UserModel
        fields = ('email', 'first_name', 'last_name',
                  'is_freelancer', 'photo', 'experience')
