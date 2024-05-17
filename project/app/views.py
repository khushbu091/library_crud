from django.shortcuts import render
from .models import *
from django.db.models import Q

# from django.shortcuts import redirect

# Create your views here.
def home(request):
    return render(request, 'home.html')
def about(request):
    return render(request, 'about.html')
def contact(request):
    return render(request, 'contact.html')
def register(request):
    return render(request, 'register.html')
def login(request):
    return render(request, 'login.html')
def registerdata(request):
    name=request.POST.get('name')
    emails=request.POST.get('email')
    contact=request.POST.get('contact')
    password=request.POST.get('password')
    cpassword=request.POST.get('cpassword')
   
    data=Student.objects.filter(Email=emails)
    print(data)

    if data:
        msg="Emails already exist" 
        return render(request,'register.html',{'key':msg})
    else:
        if password==cpassword:
            Student.objects.create(Name=name,
                                     Email=emails,
                                     Contact=contact,
                                     Password=password,
                                    )
            msg='registrations'

            return render(request,'login.html',{'key':msg})
        else:
            msg="password and Confirm Password not matched"
            return render(request,'register.html',{'key':msg})
def logindata(request):
    emails=request.POST.get('email')
    password=request.POST.get('password')
    user=Student.objects.filter(Email=emails)
    if user:
        data=Student.objects.get(Email=emails)
        pss=data.Password
        if pss==password:
            context={
                'nm':data.Name,
                'em':data.Email,
                'pass':data.Password,
                'logout':'logout'
            }
            return render(request,'dashbord.html',{'context':context})
        else:
            msg='Enter valid emails'
            return render(request,'login.html',{'key':msg})
    else:
        msg="enter valid emails"
        return render (request,'login.html',{'key':msg})
        

    # print(request.POST)

def dashbord(request):
    return render(request, 'dashbord.html')
def logout(request):
    return render(request, 'home.html')

def query(request):
    print(request.POST)
    tittle=request.POST.get('tittle')
    dec=request.POST.get('dec')
    emails=request.POST.get('email')
    password=request.POST.get('password')

    Query.objects.create(Tittle=tittle,Dec=dec,Email=emails,Password=password)
    user1 = Student.objects.get(Email=emails)
    context={
                'nm':user1.Name,
                'em':user1.Email,
                'pass':user1.Password,
                'logout':'logout'
            } 
    all_data=Query.objects.filter(Email=emails)
    return render(request,'dashbord.html',{'key':all_data,'context':context})

def showdata(request):
    print(request.POST)
    emails=request.POST.get('email')

    datas=Query.objects.filter(Email=emails)
    if datas:
       user1=Student.objects.get(Email=emails)
       context={
                'nm':user1.Name,
                'em':user1.Email,
                'pass':user1.Password,
                'logout':'logout'
            } 
       all_data=Query.objects.filter(Email=emails)
       return render(request,'dashbord.html',{'key1':all_data,'context':context})

def delete(request,pk,ml):
    sdel=Query.objects.get(id=pk)
    sdel.delete()
    eml=Query.objects.filter(Email=ml)
    msg='data delete'
    datas=Query.objects.filter(Email=ml)
    if datas:
        user1=Student.objects.get(Email=ml)
        context={
                'nm':user1.Name,
                'em':user1.Email,
                'pass':user1.Password,
                'logout':'logout'
            } 
    all_data=Query.objects.filter(Email=ml)
    return render(request,'dashbord.html',{'key1':all_data,'context':context})

def edit(request,pk,ml):
    sedt=Query.objects.get(id=pk)
    ml=Query.objects.filter(Email=ml)
    msg='edit data'
    datas=Query.objects.filter(Email=ml)
    if datas:
        user1=Student.objects.get(Email=ml)
        context={
                'nm':user1.Name,
                'em':user1.Email,
                'pass':user1.Password,
                'logout':'logout'
            } 
    all_data=Query.objects.filter(Email=ml)
    return render(request,'dashbord.html',{'key1':all_data,'context':context})

