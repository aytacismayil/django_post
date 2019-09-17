from django.urls import path
from .views import adlar

urlpatterns = [
    path("adlar/",adlar,name="adlar")
]
