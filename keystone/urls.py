from django.urls import path
from . import views

urlpatterns = [
    path('', views.model_list, name='model_list'),
    path('model/<str:model_name>/', views.model_detail, name='model_detail'),
    path('model/<str:model_name>/add/', views.model_add, name='model_add'),
]