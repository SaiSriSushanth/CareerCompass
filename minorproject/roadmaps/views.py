from django.shortcuts import render, redirect
from .models import Roadmap
from django.contrib.auth.decorators import login_required
from . import forms
# Create your views here.
def roadmaps_list(request):
    roadmaps = Roadmap.objects.all().order_by('-date')
    return render(request, 'roadmaps/roadmaps_list.html',
                   {'roadmaps': roadmaps})

def roadmap_page(request, slug):
    roadmap = Roadmap.objects.get(slug=slug)
    return render(request, 'roadmaps/roadmap_page.html',
                   {'roadmap': roadmap})

@login_required(login_url="/users/login/")
def roadmap_new(request):
    if request.method == 'POST':
        form = forms.CreatePost(request.POST, request.FILES)
        if form.is_valid():
            newroadmap = form.save(commit=False)
            newroadmap.author = request.user
            newroadmap.save()
            return redirect('roadmaps:list')
    else:
        form = forms.CreatePost()
    return render(request, 'roadmaps/roadmap_new.html',
                   {'form':form})