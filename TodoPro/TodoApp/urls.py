from django.urls import path
from TodoApp import views

urlpatterns = [
    path('demo/', views.demo, name='demo'),
    path('', views.home, name='home'),
    path('create/', views.create, name='create'),
    path('update/<int:id>', views.update, name='update'),
    path('delete/<int:id>', views.delete, name='delete'),
]
