from django.urls import path

from .views import (
    SignupPageView,
    UserProfile,
    FreelanOfficeView,
    CustomerOfficeView
    )


urlpatterns = [
    path('signup/', SignupPageView.as_view(), name='signup'),
    path('profile/<uuid:pk>/', UserProfile.as_view(), name='profile'),
    path('f_office/<uuid:pk>/', FreelanOfficeView.as_view(), name='f_office'),
    path('c_office/<uuid:pk>/', CustomerOfficeView.as_view(), name='c_office')
    ]
