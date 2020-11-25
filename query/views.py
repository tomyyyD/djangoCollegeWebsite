from django.shortcuts import render
from django.http import Http404
from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView, ListView
from django.db.models import Q
from django.http import JsonResponse

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
    context = {
        'college': college,
        'Colleges': College.objects.order_by('name'),
    }
    return render(req, 'query/details.html', context)

def About(req):
    return render(req, 'query/about.html')

def SearchResults(req):
    query = req.GET.get('q')
    object_list = College.objects.filter(
        Q(name__icontains=query or Q(nickname__icontains=query))
    )
    college_list = object_list.order_by('name')
    context = {
        'Colleges': College.objects.order_by('name'),
        'college_list': college_list,
    }
    return render(req, 'query/college_list.html', context)