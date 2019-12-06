from django.urls import path

from . import views

urlpatterns = [
    path('', views.registration, name='home'),
    path('quiz/', views.quiz, name='quiz'),
    path('result/', views.result, name='result')

]