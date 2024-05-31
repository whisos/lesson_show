from django.shortcuts import render
from event.models import *
from django.views.generic import CreateView, UpdateView, ListView, DetailView
from django.http  import HttpResponseRedirect 


def index(request):
    return render(request, 'event/index.html')

from event.forms import EditForm, AddForm

class EventListView(ListView):
    model = Event
    context_object_name = "events"
    template_name = "event/index.html"

class AddCreateView(CreateView):
    model = Event
    form_class = AddForm
    template_name = "event/add.html"
    success_url = '/'

class EditCreatekView(CreateView):
    model = Event
    form_class = EditForm
    template_name = 'event/edit.html'
    success_url = '/'

def add_evetn(request):
    if request.method == "POST":
        # print(request.POST)
        # name = request.POST.get('name')
        # print(name)
        name = request.POST.get('name')
        discripton = request.POST.get('discripton')
        time = request.POST.get('time')
        date = request.POST.get('date')
        
        
        addtask = Event(name=name, discripton=discripton, time=time, date=date)
        addtask.save()
        
    return render (request, 'event/index.html')

def edit_evetn(request):
    if request.method == "POST":
        # print(request.POST)
        # name = request.POST.get('name')
        # print(name)
        name = request.POST.get('name')
        discripton = request.POST.get('discripton')
        time = request.POST.get('time')
        date = request.POST.get('date')
        
        
        addtask = Event(name=name, discripton=discripton, time=time, date=date)
        addtask.save()
        
    return render (request, 'event/index.html')