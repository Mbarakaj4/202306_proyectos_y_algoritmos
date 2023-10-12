from django.shortcuts import redirect, render
from .models import User

# Create your views here.

# Index view
def index(request):
    if 'user' in request.session:
        return redirect("/dashboard/")
    else:
        return render(request, "auth/auth.html")


# Dashboard view
def dashboard(request):
    if 'user' in request.session:
        users = User.objects.all().order_by('-id')
        data = {
            "users": users
        }
        return render(request, "kitten/index.html", data)
    else:
        return redirect("/")


# Dashboard/clients view
def clients(request):
    if 'user' in request.session:
        users = User.objects.all()
        data = {
            "users": users
        }
        return render(request, "kitten/clients.html", data)
    else:
        return redirect("/")

# Dashboard/orders view
def orders(request):
    if 'user' in request.session:
        return render(request, "kitten/jobs.html")
    else:
        return redirect("/")

# Dashboard/clients/add function
def add_client(request):
    if 'user' in request.session:
        return render(request, "kitten/clients.html")
    else:
        return redirect("/")


# Dashboard/clients/edit function
def edit_client(request, client_id):
    if 'user' in request.session:
        return render(request, "kitten/clients.html")
    else:
        return redirect("/")


# Dashboard/clients/delete function
def delete_client(request, client_id):
    if 'user' in request.session:
        return render(request, "kitten/clients.html")
    else:
        return redirect("/")


# Dashboard/clients/view function
def view_client(request, client_id: int):
    if 'user' in request.session:
        users = User.objects.filter(id__exact=client_id)
        data = {
            "users": users
        }
        print(data)
        return render(request, "kitten/details.html", data)
    else:
        return redirect("/")


# Workorders view

def workorders(request):
    if 'user' in request.session:
        return render(request, "work_dashboard/workorders.html")
    else:
        return redirect("/")

# Workorders/details view

def workorders_details(request):
    if 'user' in request.session:
        return render(request, "work_dashboard/details.html")
    else:
        return redirect("/")