
from django.urls import path
from epanel.views import index, new, edit, delete, login, logout

# CRUD App using Models
# User Management System
urlpatterns = [
    path('index', index),
    path('new', new),
    path('edit', edit),
    path('delete', delete),
    path('', login),
    path('logout', logout),
]
