from django.urls import path

from .views import SignupPageView, UserProfile


urlpatterns = [
    path('signup/', SignupPageView.as_view(), name='signup'),
    path('profile/<int:pk>/', UserProfile.as_view(), name='profile')
    ]
