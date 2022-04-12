from django.shortcuts import render

# Create your views here.

# index.html 요청 시 불러오기
def index(request):
    return render(request, 'single_page/index.html',)

# landing.html 요청 시 불러오기
def landing(request):
    return render(request, 'single_page/landing.html',)

# about_me.html 요청 시 불러오기
def about_me(request):
    return render(request, 'single_page/about_me.html',)