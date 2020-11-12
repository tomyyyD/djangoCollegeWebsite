from django.shortcuts import render
from django.http import Http404
from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView, ListView
from django.db.models import Q

from .models import College

# Create your views here.
def home (req):
    context = {
        'Colleges': College.objects.order_by('name'),
        'title': 'College Site Home',
    }
    return render(req, 'query/home.html', context)

def details(req, ID):
    college = get_object_or_404(College, pk=ID)
    return render(req, 'query/details.html', {'college': college})

class SearchResults(ListView):
    model = College
    template_name='college_list.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = College.objects.filter(
            Q(name__icontains=query) | Q(nickname__icontains=query)
        )
        return object_list