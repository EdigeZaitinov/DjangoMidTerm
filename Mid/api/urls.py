from django.urls import path
from api import views

urlpatterns = [
    path('', views.main, name='main'),
    path('books', views.books, name='books'),
    path('journals', views.journals, name='journals'),
    path('auth/login', views.login, name='login'),
    path('auth/register', views.register, name='register'),
]
