from django.shortcuts import render
from .models import Place
from .models import Travel
# Create your views here.

def home(request):
    obj=Place.objects.all()
    obj1=Travel.objects.all()
    return render(request,'index.html',{'result':obj,'ans':obj1})

