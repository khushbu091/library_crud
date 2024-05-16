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
    email=request.POST.get('email')
    contact=request.POST.get('contact')
    password=request.POST.get('password')
    cpassword=request.POST.get('cpassword')
   
    data=Student.objects.filter(Email=email)
    print(data)

    if data:
        msg="Email already exist" 
        return render(request,'register.html',{'key':msg})
    else:
        if password==cpassword:
            Student.objects.create(Name=name,
                                     Email=email,
                                     Contact=contact,
                                     Password=password,
                                    )
            msg='registrations'

            return render(request,'login.html',{'key':msg})
        else:
            msg="password and Confirm Password not matched"
            return render(request,'register.html',{'key':msg})
def logindata(request):
    email=request.POST.get('email')
    password=request.POST.get('password')
    user=Student.objects.filter(Email=email)
    if user:
        data=Student.objects.get(Email=email)
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
            msg='Enter valid email'
            return render(request,'login.html',{'key':msg})
    else:
        msg="enter valid email"
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
    email=request.POST.get('email')
    password=request.POST.get('password')

    Query.objects.create(Tittle=tittle,Dec=dec,Email=email,Password=password)
    print("sumit",email)
    data = Query.objects.filter(Email=email)
    ans=data.values()
    print("khushi",ans)
    # tittle=data.Tittle
    # dec=data.Dec
    # email=data.Email
    # password=data.Password

    user={
        'titlle':tittle,
        'dec':dec,
        'email':email,
        'password':password,

    }  
    all_data=Query.objects.filter(Email=email)
    return render(request,'dashbord.html',{'key':all_data,'user':user})

def showdata(request):
    #select * from tablename
    #for fetching all the data of the table
    data = Query.objects.get(Email=email)
    tittle = data.Tittle
    dec = data.Dec
    email = data.Email
   
    user={
        'tittle':tittle,
        'dec':dec,
        'email':email,
        
    }
    all_data=Query.objects.filter(Email=email)
    return render(request,'dashbord.html',{'key':all_data,'user':user})