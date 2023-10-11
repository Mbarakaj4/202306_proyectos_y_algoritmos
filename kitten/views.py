from django.shortcuts import redirect, render
from django.db.models import Q
from django.contrib.auth.hashers import make_password, check_password
from .models import User

# Create your views here.

# Index view
def index(request):
    if 'user' in request.session:
        return redirect("/dashboard/")
    else:
        return render(request, "auth/auth.html")


# Auth function
def auth(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        data = {
            "email": email,
            "password": password
        }
        # print(email, password)
        try:
            user = User.objects.filter( Q(email_address__startswith=data['email']) )
        except:
            print("User not found")
            return redirect("/")
        else:
            request.session['user'] = data["email"]
            if check_password(data['password'], user[0].password):
                return redirect("/dashboard/")

# Register function
def register(request):
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        password = request.POST.get("password")
        data = {
            "first_name": first_name,
            "last_name": last_name,
            "email": email,
            "password": password,
        }
        # print(email, password, first_name, last_name)
        try:
            user = User(
                first_name=data['first_name'], 
                last_name=data['last_name'], 
                email_address=data['email'], 
                password=make_password(data['password'])
            )
        except:
            print('Something went wrong with the registration')
            return redirect("/")
        else:
            user.save()
            request.session['user'] = email
            return redirect("/dashboard/")
    

# Logout function
def logout(request):
    request.session.clear()
    return redirect("/")


# Dashboard view
def dashboard(request):
    if 'user' in request.session:
        users = User.objects.all()
        data = {
            "users": users
        }
        return render(request, "kitten/index.html", data)
    else:
        return redirect("/")


# Dashboard/clients view
def clients(request):
    if 'user' in request.session:
        return render(request, "kitten/clients.html")
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
def edit_client(request):
    if 'user' in request.session:
        return render(request, "kitten/clients.html")
    else:
        return redirect("/")


# Dashboard/clients/delete function
def delete_client(request):
    if 'user' in request.session:
        return render(request, "kitten/clients.html")
    else:
        return redirect("/")


# Dashboard/clients/view function
def view_client(request):
    if 'user' in request.session:
        return render(request, "kitten/clients.html")
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