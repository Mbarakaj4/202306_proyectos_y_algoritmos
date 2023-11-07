from django.shortcuts import redirect, render
from .models import User, Job


def index(request):
    if "user" in request.session:
        return redirect("/dashboard/")
    else:
        return render(request, "auth/auth.html")


def dashboard(request):
    if "user" in request.session:
        users = User.objects.all().order_by("-id")
        orders = Job.objects.all()
        data = {"orders": orders,
                "users": users
        }
        return render(request, "kitten/index.html", data)
    else:
        return redirect("/")


def error404(request):
    return render(request, "kitten/404.html")


def clients(request):
    if "user" in request.session:
        users = User.objects.all()
        data = {"users": users}
        return render(request, "kitten/clients.html", data)
    else:
        return redirect("/")


def orders(request):
    if "user" in request.session:
        orders = Job.objects.all()
        data = {"orders": orders}
        return render(request, "kitten/orders.html", data)
    else:
        return redirect("/")


def add_client(request):
    if "user" in request.session:
        return redirect("error404")
    else:
        return redirect("/")


def edit_client(request, client_id):
    if "user" in request.session:
        users = User.objects.filter(id__exact=client_id)
        data = {
            "users": users,
            "action": "Editar cliente"
        }
        print(data)
        return render(request, "kitten/details.html", data)
    else:
        return redirect("/")


def delete_client(request, client_id):
    if "user" in request.session:
        return redirect("error404")
    else:
        return redirect("/")


def view_client(request, client_id: int):
    if "user" in request.session:
        users = User.objects.filter(id__exact=client_id)
        data = {
            "users": users,
            "action": "Ver cliente"
        }
        print(data)
        return render(request, "kitten/details.html", data)
    else:
        return redirect("/")


def workorders(request):
    if "user" in request.session:
        return render(request, "work_dashboard/workorders.html")
    else:
        return redirect("/")


def workorders_details(request):
    if "user" in request.session:
        return render(request, "work_dashboard/details.html")
    else:
        return redirect("/")
