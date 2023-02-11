from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
class Weapon(models.Model):
    name = models.CharField(max_length=50)
    lethal= models.CharField(max_length=20)

    def __str__ (self):
        return f'{self.name} {self.lethal}'
    def get_absolute_urls(self):
        return reverse('weapons_detail', kwargs={'pk': self.id})

class Person(models.Model):
    name = models.CharField(max_length=50, default="Unknown")
    type = models.CharField(max_length=50, default='Unknown')
    description = models.TextField(max_length=250, default= 'None provided')
    age = models.IntegerField(null = True)
    weapons = models.ManyToManyField(Weapon)

def __str__(self):
    return self.name

def get_absolute_url(self):
    return reverse('detail',kwargs={'person_id':self.id})

class Location(models.Model):
    location = models.TextField(max_length=100)
    date = models.DateField()
    time = models.TimeField()

    person = models.ForeignKey(Person, on_delete=models.CASCADE)

def __str__(self):
    return f"{Person.name} was last seen on {self.location} at {self.time}"


class Photo(models.Model):
    url = models.CharField(max_length=200)
    person = models.ForeignKey(Person, on_delete= models.CASCADE)

    # def __str__(self):
    #     return f"Photo for person: {self.person.name} {@self.url}"


    ## Left off added your second model which is a One to one relationship