from django.shortcuts import render, HttpResponse,redirect
from .models import *
from django.contrib import messages
import bcrypt

def index(request):
    return render (request,'login.html')

def register(request):
    if request.method =='POST':
        errors = User.objects.basic_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/')
        else:
            fname = request.POST['fname']
            lname = request.POST['lname']
            email = request.POST['email']
            password = request.POST['password']
            pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()  
            print(pw_hash)
            request.session['username'] = fname + " "+ lname
            request.session['status']="Registered"
            User.objects.create(first_name=fname, last_name=lname,email=email, password=pw_hash)
    return redirect("/")
def login(request):
    if request.method =='POST':
        errors2 = User.objects.login_validator(request.POST)
        if len(errors2) > 0:
            for key, value in errors2.items():
                messages.error(request, value)
            return redirect('/')

        users = User.objects.filter(email=request.POST['email2'])
        if users:
            logged_user = users[0]
            if bcrypt.checkpw(request.POST['password2'].encode(), logged_user.password.encode()):
                request.session['username'] = logged_user.first_name
                request.session['status']="logged in"
                request.session['user_id'] = logged_user.id
                return redirect('/classes')
            print("""Wrong password""")
        return redirect("/")
def classes(request):
    return render(request,'cource.html')
def create_cource(request):
    if request.method =='POST':
        user_id = request.session['user_id']
        errors = Cource.objects.cource_validation(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
        else:
            name = request.POST['name'] 
            day = request.POST['day'] 
            price = request.POST['price'] 
            desc = request.POST['desc'] 
            user = User.objects.get(id = user_id)
            Cource.objects.create(
                name = name,
                day = day,
                price = price,
                desc = desc,
                user = user
            )
    return redirect('/classes/new') 
def table(request):
    context = {
        'all_cources': Cource.objects.all(),
        'user': User.objects.get(id = request.session['user_id'] )
    }
    return render (request,'classes.html',context) 

def edit(request,id):
    context={
        'cource':Cource.objects.get(id = id)
    } 
    
            
    return render(request,'edit.html',context)
    

def edit_form(request,id):
    if request.method =='POST':
        
        errors = Cource.objects.cource_validation(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
               
            
                   
        else:
            cource_update = Cource.objects.get(id = id)
            cource_update.name = request.POST['name'] 
            cource_update.day = request.POST['day'] 
            cource_update.price = request.POST['price'] 
            cource_update.desc = request.POST['desc'] 
            cource_update.save()
            
        return redirect('/classes') 

def details(request,id):
        context = {
            'cource':Cource.objects.get(id = id)
        }
        return render(request,'details.html',context) 
def delete(request,id):
    cource_delete = Cource.objects.get(id = id)
    cource_delete.delete()
    return redirect('/classes') 

def logout(request):
    del request.session['username']
    del request.session['status']
    request.session['user_id']
   
    return redirect('/')   
    
    

