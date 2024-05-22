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
    path('delete/<int:pk>/',delete,name='delete'),
    path('edit/<int:pk>/',edit,name='edit'),
    path('update/<int:pk>/',update,name='update')



    # path('showdata/',showdata,name='showdata')
    # path('logout',logout,name='logout')


]
