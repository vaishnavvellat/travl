from django.http import HttpResponse
from django.shortcuts import render
from  . models import mud
from . models import axe

# Create your views here.

def demo(request):
    obj=mud.objects.all()
    obj1=axe.objects.all()
    return render(request, "index.html",{'result':obj,'results':obj1})










