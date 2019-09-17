from django.urls import path
from .views import *

urlpatterns = [
    path("title/",titlee,name="title")
]
