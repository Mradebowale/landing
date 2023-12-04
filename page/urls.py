from django.urls import path
from .views import landing, contactpage

urlpatterns = [
     path('', landing, name='home'),
    path('contact/', contactpage, name='contact'),
]