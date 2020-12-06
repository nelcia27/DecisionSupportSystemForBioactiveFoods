from django.urls import path

from . import views

urlpatterns = [
    path('', views.generate_experiment_excel, name='generate_experiment_excel'),
]