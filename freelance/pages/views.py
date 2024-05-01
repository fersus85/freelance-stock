from django.views.generic import TemplateView, ListView
from django.contrib.auth import get_user_model
from django.db.models import Q


UserModel = get_user_model()


class HomePageView(TemplateView):
    template_name = 'home.html'


class AboutPageView(TemplateView):
    template_name = 'about.html'


class SearchResultListView(ListView):
    model = UserModel
    context_object_name = 'results'
    template_name = 'search_results.html'

    def get_queryset(self):
        querry = self.request.GET.get('q')
        return UserModel.objects.filter(
            Q(experience__icontains=querry) |
            Q(first_name__icontains=querry) |
            Q(last_name__icontains=querry)
        )
