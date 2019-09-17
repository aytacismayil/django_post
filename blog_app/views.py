from django.shortcuts import render
from .models import Blog
from .forms import Title

  # Create your views here.
def titlee(request):

    c={
        'adi':Title   
    }

    if request.method=="POST":
        f = Title(request.POST)
        if f.is_valid():
            f.save()
          # else:
          #     c['errors']=f.errors

    return render(request,'blog.html',context=c)