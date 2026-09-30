from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from finance.models import Operations, User


@login_required
def index(request):



    return render(request, 'dashboard/index.html', context={'username':request.user.username})



# Create your views here.
@login_required
def dashboard(request):

    operations = Operations.objects.all()

    return  render(request,"dashboard/dashboard.html", context={'operations':operations, 'users':User.objects.all()})


@login_required
def historizes(request):
    return render(request, "dashboard/historique.html")


def login_user(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)


        if user:
            login(request, user)

            return redirect('index')

    return render(request, 'login/login.html')
