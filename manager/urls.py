from django.urls import path
from . import views

urlpatterns = [
    path('contact_form/', views.get_contact_form, name='get_contact_form'),
    path('search/', views.search, name='search'),
    path('', views.create, name='list_create'),
    path('update/<int:id>/', views.update, name='update'),
    path('delete/<int:id>/', views.delete, name='delete'),
 ]