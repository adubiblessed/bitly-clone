from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from .models import Link
from .forms import Linkform

# Create your views here.
def index(request):
    links =Link.objects.all()
    context = {
        "links":links
    }
    return render(request, 'links/index.html', context)

def root_link(request, link_slug):
    link = get_object_or_404(Link, slug=link_slug)
    link.click()

    return redirect(link.url)

def add_link(request):
    if request.method == 'POST':
        #form has data
        form = Linkform(request.POST)
        if form.is_valid():
            #save the data
            form.save()
            return redirect(reverse('home'))
    else:
        form = Linkform()
    context = {
        "form":form
    }
    return render(request, 'links/create.html', context)