from django.urls import path
from googletakvim import views

urlpatterns = [
    path('', views.index, name='index')
]
