from django.urls import path
from . import views

app_name = 'author'

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('update/<int:author_id>/', views.update, name='update'),
    path('delete/<int:author_id>/', views.delete, name='delete'),
]