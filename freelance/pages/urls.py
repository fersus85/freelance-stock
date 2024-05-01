from django.urls import path
from .views import HomePageView, AboutPageView, SearchResultListView


urlpatterns = [
 path('', HomePageView.as_view(), name='home'),
 path('about/', AboutPageView.as_view(), name='about'),
 path('search/', SearchResultListView.as_view(), name='search_results')
 ]
