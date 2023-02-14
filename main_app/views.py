from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Person, Weapon, Photo
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

import boto3
import uuid
# Create your views here.

S3_BASE_URL ='https://s3.us-east-1.amazonaws.com/'
BUCKET = 'LastSurvivalKit'

def home(request):
    return render(request,'Home.html')

def about(request):
    return render(request,"about.html")
@login_required
def people_index(request):
    people = Person.objects.filter(user = request.user)
    return render(request,'people/index.html',{'people':people})
@login_required
def people_detail(request,person_id):
    person = Person.objects.get(id= person_id)
    unarmed = Weapon.objects.exclude(id__in= person.weapons.all().values_list('id'))
    return render(request,'people/detail.html',{'person':person,
    'wepaons': unarmed})

@login_required
def add_photo(request, person_id):
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 =boto3.client('s3')
        key = uuid.uuid4().hex[:6] + photo_file.name [photo_file.name.rfind('.'):]

        try:
            s3.upload_fileobj(photo_file, BUCKET, key)

            url = f"{S3_BASE_URL}{BUCKET}/{key}"

            photo = Photo(url=url, person_id=person_id)

            photo.save()
        except Exception as error:
            print('something went wrong uploading to s3')
        return redirect('detail', person_id=person_id)
@login_required
def assoc_weapon(request, person_id,weapon_id):
    Person.objects.get(id=person_id).weapons.add(weapon_id)
    return redirect('detail',weapon_id=weapon_id)

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('index')
    else:
        error_message = 'invalid credentials'
    form = UserCreationForm()
    return render(request, 'registration/signup.html', {
            'form': form,
            'error': error_message
        })

def logout_view(request):
    logout(request)
    return redirect('/')
    
class PersonCreate(LoginRequiredMixin,CreateView):
    model = Person
    fields = ['name','type', 'description','age']
    success_url = '/people/'

    def form_valid(self,form):
        form.instance.user =self.request.user
        return super().form_valid(form)

class PersonUpdate(LoginRequiredMixin,UpdateView):
    model = Person
    fields = ['type', 'description','age']
    success_url = '/people/'

class PersonDelete(LoginRequiredMixin,DeleteView):
    model = Person
    success_url = '/people/'

class WeaponIndex(LoginRequiredMixin,ListView):
    model = Weapon

class WeaponDetail(LoginRequiredMixin,DetailView):
    model = Weapon

class WeaponCreate(LoginRequiredMixin,CreateView):
    model= Weapon
    fields = '__all__'
    success_url = '/weapons/'

class WeaponUpdate(UpdateView):
    model = Weapon
    fields ='__all__'
    success_url = '/weapons/'

class WeaponDelete(DeleteView):
    model = Weapon
    success_url = '/weapons/'