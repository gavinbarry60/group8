from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Feature
from .models import UserProfile
from django.contrib.auth.decorators import login_required


# Create your views here.

def index(request):

    features = Feature.objects.all()

    return render(request, 'index.html', {'features': features})

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        
        #checks for errors with making credentials
        #we can edit this to fit requirements for project
        if password1 == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email Already Used')
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username Already Used')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, email=email, password=password1)
                user.save();
                UserProfile.objects.create(user=user, role='buyer')
                return redirect('login')
        else:
            messages.info(request, 'Password Not the Same')
            return redirect('register')
    else:
        return render(request, 'register.html')

@login_required
def nileAccountDeletion(request):
    if request.method == "POST":
        user = request.user
        logout(request)
        user.delete()
        messages.success(request, "Your account has been deleted.")
        return redirect('/')
    return render(request, 'nileAccountDeletion')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Credentials Invalid')
            return redirect('login')

    return render (request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')


def counter(request):
    posts = [1, 2, 3, 4, 5, 'tim', 'tom', 'john']
    return render(request, 'counter.html', {'posts': posts})

def post(request, pk):
    return render(request, 'post.html', {'pk': pk})

def nileHomePage(request):
    return render(request, 'nileHomePage.html')

def nileAccountInfo(request):
    return render(request, 'nileAccountInfo.html')

def nileCreateAccount(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        
        #checks for errors with making credentials
        #we can edit this to fit requirements for project
        if password1 == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email Already Used')
                return redirect('nileCreateAccount')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username Already Used')
                return redirect('nileCreateAccount')
            else:
                user = User.objects.create_user(username=username, email=email, password=password1)
                user.save();
                UserProfile.objects.create(user=user, role='buyer')
                return redirect('nileLogin')
        else:
            messages.info(request, 'Password Not the Same')
            return redirect('nileCreateAccount')
    else:
        return render(request, 'nileCreateAccount.html')

    return render(request, 'nileCreateAccount.html')

def nileLogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Credentials Invalid')
            return redirect('nileLogin')

    return render(request, 'nileLogin.html')

def nileProducts(request):
    return render(request, 'nileProducts.html')

def nileAccountSettings(request):
    return render(request, 'nileAccountSettings.html')

@login_required
def nileAccountInfo(request):
    user = request.user
    try:
        profile = UserProfile.objects.get(user=user)
        role = profile.role
    except UserProfile.DoesNotExist:
        role = "Unknown"  # fallback if profile is missing

    return render(request, 'nileAccountInfo.html', {'role': role})    
