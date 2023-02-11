from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Person, Weapon, Photo
from django.contrib.auth.forms import UserCreationForm

import boto3
import uuid
# Create your views here.

def home(request):
    return render(request,'Home.html')

def about(request):
    return render(request,"about.html")

def people_index(request):
    people = Person.objects.all()
    return render(request,'people/index.html',{'people':people})

def people_detail(request,person_id):
    person = Person.objects.get(id= person_id)
    unarmed = Weapon.objects.exclude(id__in= person.weapons.all())
    return render(request,'people/detail.html',{'person':person,
    'wepaons': unarmed})

def add_photo(request, person_id):
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 =boto3.client('s3')
        key = uuid.uuid4().hex[:6] + photo_file.name [photo_file.name.rfind('.'):]

        try:
            s3.upload_fileobj(photo_file, Bucket, key)

            url = f"{S3_BASE_URL}{BUCKET}/{key}"

            photo = Photo(url=url, person_id=person_id)

            photo.save()
        except Exception as error:
            print('something went wrong uploading to s3')
            print(error)

def assoc_weapon(request, person_id,weapon_id):
    Person.objects.get(id=person_id).weapons.add(weapon_id)
    return redirect('detail',weapon_id=weapon_id)

class PersonCreate(CreateView):
    model = Person
    fields = '__all__'
    success_url = '/People/'

class PersonUpdate(UpdateView):
    model = Person
    fields = ['type', 'description','age']

class PersonDelete(DeleteView):
    model = Person
    success_url = '/people/'

class WeaponIndex(ListView):
    model = Weapon
class WeaponDetail(DetailView):
    model = Weapon

class WeaponCreate(CreateView):
    model= Weapon
    fields = '__all__'

class WeaponUpdate(UpdateView):
    model = Weapon
    fields ='__all__'

class WeaponDelete(DeleteView):
    model = Weapon
    success_url = '/People/'