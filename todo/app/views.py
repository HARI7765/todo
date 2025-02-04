from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.
def main(request):
    if request.POST:
        name=request.POST.get('name')
        email=request.POST.get('email')
        obj1=UserProfile(name=name,email=email)
        obj1.save()
    return render(request,"main.html")