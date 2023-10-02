from django.shortcuts import redirect, render

# Create your views here.

# Index view
def index(request):
    return render(request, "auth/auth.html")


# Auth function
def auth(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        request.session['user'] = email
        print(email, password)
        return redirect("/dashboard/")


# Register function
def register(request):
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        password = request.POST.get("password")
        request.session['user'] = email
        print(email, password, first_name, last_name)
        return redirect("/dashboard/")
    

# Logout function
def logout(request):
    request.session.clear()
    return redirect("/")


# Dashboard view
def dashboard(request):
    if 'user' in request.session:
        return render(request, "kitten/index.html")
    else:
        return redirect("/")