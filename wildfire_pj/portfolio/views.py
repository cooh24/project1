from django.shortcuts import render

# Create your views here.

def port1(request):
    return render(request, 'portfolio/port1.html',)
def port2(request):
    return render(request, 'portfolio/port2.html',)
def port3(request):
    return render(request, 'portfolio/port3.html',)
def port4(request):
    return render(request, 'portfolio/port4.html',)