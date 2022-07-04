from django.shortcuts import render # html file -> output
from django.http import HttpResponse # text (html tags) -> output
# Create your views here.

def index(request):
    return render(request, 'app1_4/index.html')

def blog(request):
    return render(request, 'app1_4/blog.html')

def career(request):
    return render(request, 'app1_4/career.html')

def contact(request):
    return render(request, 'app1_4/contact_us.html')

def offers(request):
    return render(request, 'app1_4/offers.html')

def onlineadmission(request):
    return render(request, 'app1_4/online_admission.html')

def paymentoption(request):
    return render(request, 'app1_4/payment_option.html')

def successgalley(request):
    return render(request, 'app1_4/success_gallery.html')

def testimonials(request):
    return render(request, 'app1_4/testimonials.html')

# Task-1
"""
Create the following html files, render and display.
    Success Gallery
    Testimonials
    Online Admission
    Payment Option
    Offers
    Career
    Contact Us
    Blog
"""