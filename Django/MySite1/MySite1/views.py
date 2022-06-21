from django.http import HttpResponse

def function1(request):
	return HttpResponse("Hello world of Django")

def function2(request):
	return HttpResponse("About Us")

def function3(request):
	return HttpResponse("Services")