from django.shortcuts import render

# Create your views here.

# Index view
def index(request):
    return render(request, "auth/auth.html")

# Auth function
def auth(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        print(email, password)
        return render(request, "kitten/index.html")
    
# Register function
def register(request):
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        password = request.POST.get("password")
        print(email, password, first_name, last_name)
        return render(request, "kitten/index.html")
    return render(request, "auth/auth.html")