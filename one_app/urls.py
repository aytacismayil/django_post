from django.urls import path
from .views import mehsul_yarat

urlpatterns = [
    path('mehsul_yarat/',mehsul_yarat,name='mehsul_yarat')
]
