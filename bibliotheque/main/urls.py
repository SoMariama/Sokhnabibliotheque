from django.urls import path
from main import views

urlpatterns = [
    path('',views.home),
    path('contact/',views.contact)
]
