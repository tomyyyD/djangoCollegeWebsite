from django.shortcuts import render
from django.http import Http404
from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView, ListView
from django.db.models import Q
from django.http import JsonResponse

from .models import College

# Create your views here.
def home (req):
    if 'term' in req.GET:
        qs = College.objects.filter(name__icontains=req.GET.get("term"))
        names = list()
        for college in qs:
            names.append(college.name)
        return JsonResponse(names, safe=False)
    context = {
        'Colleges': College.objects.order_by('name'),
        'title': 'College Site Home',
    }
    return render(req, 'query/home.html', context)

def details(req, ID):
    if 'term' in req.GET:
        qs = College.objects.filter(name__icontains=req.GET.get("term"))
        names = list()
        for college in qs:
            names.append(college.name)
        return JsonResponse(names, safe=False)

    college = get_object_or_404(College, pk=ID)
    return render(req, 'query/details.html', {'college': college})

def About(req):
    return render(req, 'query/about.html')

class SearchResults(ListView):
    model = College
    template_name='college_list.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = College.objects.filter(
            Q(name__icontains=query) | Q(nickname__icontains=query)
        )
        college_list = object_list.order_by("name")
        return college_list

