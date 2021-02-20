from django.urls import path     
from . import views

urlpatterns = [
    path('', views.index),	 
	path('add_user', views.add_user)  ,
	path('add_dojo', views.add_dojo)
]