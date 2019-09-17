from django.urls import path
from .views import *

urlpatterns = [
    path("com/",com,name="comment")
]
