from django.shortcuts import render
from .forms import Student
# Create your views here.
def register(request):
    fm=Student()
    return render(request,'regi/home.html',{'form':fm})
