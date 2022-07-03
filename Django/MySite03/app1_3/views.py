from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.
def index(request):
    str1 = """
    <html>
        <head>
             <title>MyFirst Page</title>
        </head>
        <body>
            <h1>Welcome to app1_3</h1>
        </body>
    </html>
    """
    return HttpResponse(str1);
