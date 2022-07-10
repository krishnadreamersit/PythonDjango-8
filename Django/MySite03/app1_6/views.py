from django.shortcuts import render


def index(request):
    return render(request, 'app1_6/index.html');