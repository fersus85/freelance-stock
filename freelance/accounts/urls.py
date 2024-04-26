from django.urls import path

from .views import RegistrationPageView


urlpatterns = [
    path('signup/', RegistrationPageView.as_view(), name='signup'),
]
