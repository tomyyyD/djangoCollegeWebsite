from django.shortcuts import render
from django.http import Http404
from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView, ListView
from django.db.models import Q, Count
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
    if req.GET.get('q'):
        query = req.GET.get('q')
        object_list = College.objects.filter(
            Q(name__icontains=query) or Q(nickname__icontains=query)
        )
        college_list = object_list.order_by('name')
        if not college_list.exists():
            return render(req, 'query/home.html')
        ID = college_list.first().pk
    college = get_object_or_404(College, pk=ID)
    context = {
        'college': college,
        'Colleges': College.objects.order_by('name'),
    }
    return render(req, 'query/details.html', context)

def About(req):
    return render(req, 'query/about.html')

def SearchResults(req):
    if req.GET.get('q'):
        query = req.GET.get('q')
        object_list = College.objects.filter(
            Q(name__icontains=query)
        )
        nickname_list = College.objects.filter(
            Q(nickname__icontains=query)
        )
        full_list = object_list | nickname_list
        full_list = full_list.order_by('name')
    elif req.GET.get('s'):
        query = req.GET.get('s')
        object_list= College.objects.filter(
            Q(state__icontains=query)
        )
        full_list = object_list.order_by('state')
    context = {
        'Colleges': College.objects.order_by('name'),
        'college_list': full_list,
    }
    return render(req, 'query/college_list.html', context)