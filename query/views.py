from django.shortcuts import render, redirect
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
        'States': College.objects.values('state').distinct().order_by('state'),
        'title': 'College Site Home',
    }
    return render(req, 'query/home.html', context)

def details(req, nickname):
    if req.GET.get('q'):
        query = req.GET.get('q')
        object_list = College.objects.filter(
            Q(name__icontains=query) or Q(nickname__icontains=query)
        )
        college_list = object_list.order_by('name')
        if not college_list.exists():
            return render(req, 'query/home.html')
        nickname = college_list.first().nickname
        return redirect('details', nickname)
    college = get_object_or_404(College, nickname=nickname)
    context = {
        'college': college,
        'Colleges': College.objects.order_by('name'),
    }
    return render(req, 'query/details.html', context)

def About(req):
    return render(req, 'query/about.html')

def SearchResults(req):
    full_list = College.objects.order_by('name')
    nameQuery = ''
    stateQuery = ''
    if req.GET.get('q'):
        nameQuery = req.GET.get('q')
        print(nameQuery)
        if nameQuery == 'Name':
            pass
        else:
            object_list = full_list.filter(
                Q(name__icontains=nameQuery)
            )
            nickname_list = full_list.filter(
                Q(nickname__icontains=nameQuery)
            )
            full_list = object_list | nickname_list
            full_list = full_list.order_by('name')
            #print(full_list)
    if req.GET.get('s'):
        stateQuery = req.GET.get('s')
        if stateQuery == 'State':
            pass
        else:
            state_list = full_list.filter(
                Q(state__icontains=stateQuery)
            )
            #print(state_list)
            full_list = state_list.order_by('state')
    context = {
        'Colleges': College.objects.order_by('name'),
        'States': College.objects.values('state').distinct().order_by('state'),
        'college_list': full_list,
        'currState': stateQuery,
        'currName': nameQuery,
    }
    return render(req, 'query/college_list.html', context)