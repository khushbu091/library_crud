# from django.contrib import admin
from django.urls import *
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),  
    path('register/', register, name='register'),
    path('login/', login, name='login'),
    path('registerdata/', registerdata, name='registerdata'),
    path('logindata/', logindata, name='logindata'),
    path('dashbord/', dashbord, name='dashbord'),
    path('query/',query,name='query'),
    path('showdata/',showdata,name='showdata'),
    path('delete/<int:pk>/<ml>',delete,name='delete'),
    path('edit/<int:pk>/<ml>',edit,name='edit'),




    # path('showdata/',showdata,name='showdata')
    # path('logout',logout,name='logout')


]
