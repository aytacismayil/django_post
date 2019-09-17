from django.shortcuts import render
from .models import Author
from .forms import Ad

 # Create your views here.
def adlar(request):  
    c={
         'adi':Ad      
    }
    if request.method=="POST":
        f = Ad(request.POST)
        if f.is_valid():
            f.save()    
    return render(request,'author.html',context=c)