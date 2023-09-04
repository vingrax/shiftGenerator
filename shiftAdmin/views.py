from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def shiftCreateView(request):
    return render(request,'shiftAdmin/createShift.html')