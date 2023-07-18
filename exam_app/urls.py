from django.urls import path   
from . import views
urlpatterns = [ path('', views.index),
                path('register', views.register),
                 path('login', views.login),
                  path('classes/new', views.classes),
                  path('create', views.create_cource,name='create_cource'),
                  path('classes', views.table),
                  path('edit/<int:id>', views.edit_form,name='edit_cource'),
                   path('classes/<int:id>/edit', views.edit, name='edit'),
                   path('classes/<int:id>', views.details, name='details'),
                   path('delete<int:id>', views.delete, name='delete'),
                   path('logout', views.logout, name='logout'),
                   
                  ]