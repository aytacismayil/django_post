from django.shortcuts import render
from .models import Comment
from .forms import Coment
# Create your views here.
def com(request):
    c={
        'adi':Coment
    }
    if request.method =="POST":
        t= Coment(request.POST)
        if t.is_valid():
           t.save()
    return render(request,'comment.html',context=c)