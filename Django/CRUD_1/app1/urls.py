from django.urls import path
from app1.views import index, addnew, savenew, displayedit, update, delete

urlpatterns = [
    path('', index),
    path('new/', addnew),
    path('save/', savenew),
    path('edit', displayedit),
    path('update', update),
    path('delete', delete),
]
