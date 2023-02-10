from django.urls import path
from . import views


urlpatterns =[
    path('',views.home, name='home'),
    path('about/', views.about, name='about'),
    path('People/',views.people_index, name='index'),
    path('people/<int:person_id>/',views.people_detail, name = 'detail'),
    path('people/create/',views.PersonCreate.as_view(), name='people_create'),
    path('people/<int:pk>/update/', views.PersonUpdate.as_view(),name='people_update'),
    path('people/<int:pk>/delete/', views.PersonDelete.as_view(),name='people_delete'),
    path('people/<int:person_id>/assoc_weapons/<int:weapon_id>/', views.assoc_toy, name='assoc_weapon'),
]