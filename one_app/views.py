from django.shortcuts import render
from .models import Products
from .forms import Mehsulelaveet

# Create your views here.
def mehsul_yarat(request):

    c={
        'yaratma_formasi': Mehsulelaveet,
        'errors':''
    }
    # print(request.method)
    if request.method =="POST" :
        f = Mehsulelaveet(request.POST , request.FILES)
        if f.is_valid():
            f.save()
        else:
            c['errors']=f.errors
            
        # name =request.POST.get('name')
        # price = request.POST.get('price')
        # image = request.POST.get('image')
        # deyer = request.POST.get('deyer')

        # Products.objects.create(name=name,price=price,image=image,deyer=deyer)
        
    return render(request,'mehsul_yarat.html',context=c)