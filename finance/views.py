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

    if request.method == "POST":
        owner = User.objects.get(username=request.POST.get("owner"))
        new_operations = Operations.objects.create(
            name = request.POST.get("name"),
            description = request.POST.get("description"),
            price = request.POST.get("price"),
            user = owner,
            shared = request.POST.get("shared") == 1,
            type = request.POST.get("type"),
            repeat=request.POST.get("repeat") == 1,
        )
        if request.headers.get("HX-Request"):
            context = {
                "operations": Operations.objects.select_related("user").order_by("-date"),
            }
            return render(request, "dashboard/table.html", context)

            # Requête classique (sans JS) : redirection habituelle
        return redirect("dashboard")

    context = {
        "users": User.objects.all(),
        "operations": Operations.objects.select_related("user").order_by("-date"),
    }
    return render(request, "dashboard/dashboard.html", context)


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
