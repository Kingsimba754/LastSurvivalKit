from django.contrib import admin
from .models import Person, Weapon,Photo

# Register your models here.
admin.site.register(Person)
admin.site.register(Weapon)
admin.site.register(Photo)