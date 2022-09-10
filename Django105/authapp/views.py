from django.shortcuts import render
from authapp.forms import UserForm, UserProfileInfoForm

# this impoert is for the 2nd phase of this code which is for login page
from django.contrib.auth import authenticate, login,logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# scroll down to create login/logout view

# Create your views here.
def index(request):
    return render(request, 'authapp/index.html')

def base(request):
    return render(request, 'authapp/base.html')


def main(request):
    return render(request, 'authapp/main.html')



# just a special response
@login_required
def special(request):
    return HttpResponse("You are logged in, Welcome")

# creating my logout function
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


def register(request):
    
    # making sure not auto register
    registered = False
    
    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)
        
        # checking if they forms are valid
        if user_form.is_valid() and profile_form.is_valid():
            
            user = user_form.save()
            # hatching the password
            user.set_password(user.password)
            user.save()
            
            profile = profile_form.save(commit=False)
            profile.user = user
            
            # checking if they actually provided a pic
            
            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']
                
            profile.save()
            
            # now saving up 
            registered = True
            
            # returning error if userform is invalid
        else:
            print(user_form.errors,profile_form.errors)   
        
     # checking error if it was not a POST request
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()
    return render(request, 'authapp/registration.html',
                  {'user_form':user_form,
                   'profile_form':profile_form,
                   'registered':registered})
    
    
    
# login views

def user_login(request):
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # django authentication function settup
        user = authenticate(username=username,password=password)
        
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            
            else:
                return HttpResponse("ACCOUNT NOT ACTIVE")
        else:
            print("Someone tried to login and failed!")
            print("Username: {} and password {}".format(username,password))
            return HttpResponse("Invalid login details suplied!")
        
    else:
        return render(request, 'authapp/login.html')
    
