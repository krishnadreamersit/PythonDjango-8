from django.shortcuts import render


def index(request):
    return render(request, 'app1_5/index.html')
