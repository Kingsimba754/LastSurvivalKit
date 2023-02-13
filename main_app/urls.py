from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


urlpatterns =[
    path('',views.home, name='home',),
    path('logout/',views.logout_view, name='logout'),
    path('login/',auth_views.LoginView.as_view(), name="login"),
    path('about/', views.about, name='about'),
    path('people/',views.people_index, name='index'),
    path('people/<int:person_id>/',views.people_detail, name = 'detail'),
    path('people/create/',views.PersonCreate.as_view(), name='people_create'),
    path('people/<int:pk>/update/', views.PersonUpdate.as_view(),name='people_update'),
    path('people/<int:pk>/delete/', views.PersonDelete.as_view(),name='people_delete'),
    path('people/<int:person_id>/add_photo/', views.add_photo, name='add_photo'),
    path('people/<int:person_id>/assoc_weapon/<int:weapon_id>/', views.assoc_weapon, name='assoc_weapon'),
    path('weapons/create/', views.WeaponCreate.as_view(), name='weapons_create'),
    path('weapons/', views.WeaponIndex.as_view(), name='weapons_index'),
    path('weapons/<int:pk>/', views.WeaponDetail.as_view(), name='weapons_detail'),
    path('weapons/<int:pk>/update/', views.WeaponUpdate.as_view(), name='weapons_update'),
    path('weapons/<int:pk>/delete/', views.WeaponDelete.as_view(), name='weapons_delete'),
    path('accounts/signup/',views.signup, name='signup'),
    

]