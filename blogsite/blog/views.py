from django.shortcuts import render

# Create your views here.


def homepage(request):
    return render(request, 'blog/homepage.html')


def deatail(request):
    return render(request, 'blog/detail.html')


