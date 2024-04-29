from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model

from .forms import CustomUserCreationForm, ProfileForm


class SignupPageView(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


class UserProfile(LoginRequiredMixin, generic.UpdateView):
    model = get_user_model()
    form_class = ProfileForm
    template_name = 'profile.html'

    def get_success_url(self) -> str:
        return reverse_lazy('profile', args=[self.request.user.pk])
