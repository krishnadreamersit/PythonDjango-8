from django.urls import path
from app1_4.views import *

urlpatterns = [
    path('index/', index),
    path('blog/', blog),
    path('carrer/', career),
    path('contact/', contact),
    path('offer/', offers),
    path('onlineadmission/', onlineadmission),
    path('paymentoption/', paymentoption),
    path('successgalley/', successgalley),
    path('testimonials/', testimonials),
]