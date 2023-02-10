from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Person
from django.http import HttpResponse
# Create your views here.

def home(request):
    return HttpResponse('<h1>Hello!</h1>')
def about(request):
    return render(request,"about.html")

def people_index(request):
    people = Person.objects.all()
    return render(request,'people/index.html',{'people':people})

def people_detail(request,person_id):
    person = Person.objects.get(id= person_id)
    unarmed = Weapon.objects.exclude(id_in = person.weapons.all())
    return render(request,'people/detail.html',{'person':person,
    'wepaons': unarmed})

class PersonCreate(CreateView):
    model = Person
    fields = '__all__'
    success_url = '/people/'

class PersonUpdate(UpdateView):
    model = Person
    fields = ['type', 'description','age']

class PersonDelete(DeleteView):
    model = Person
    success_url = '/people/'