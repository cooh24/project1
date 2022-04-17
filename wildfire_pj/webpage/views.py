from django.shortcuts import render

# Create your views here.
def web1(request):
    return render(request, 'webpage/web1.html',)
def web2(request):
    return render(request, 'webpage/web2.html',)
def web3(request):
    return render(request, 'webpage/web3.html',)