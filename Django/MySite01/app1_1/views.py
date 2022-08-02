from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hi, from MySite001->app1_1->views->index()!!")