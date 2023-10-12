# Creating a project on Django

This notes are based on the django tutorial maded by techlearners.
I saw this as a very cool form of remind myself the process of
creating a Django project.

## Prequisites
- Install python3
- Install django
- Install vscode
## Steps

**Step 1** - *Open vscode on project folder*
**Step 2** - *Open terminal and install django*
```
pip install django
```
**Step 3** - *Create django project*
```
django-admin startproject gestion_clientes .
```
NOTE: Avoid naming the project like in the list mentioned on the
Django documentation.
**Step 4** - *Create an app*
```
django-admin startapp bot_telegram
django-admin startapp dashboard
```
**Step 5** - *Add the app on projectname/settings.py*

```python
# It should look like this
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'dashboard',
    'bot_telegram',
]
```
**Step 6** - *Run the server, check if everything works and then stop it*
```
python3 manage.py runserver
```
**Step 7** - *Migrate* (Pending research)
```
python3 manage.py migrate
```
**Step 8** - *Create superuser*
```
python3 manage.py createsuperuser
```
**Step 9** - *Check credential by login into admin*
**Step 10** - *Create templates directory inside the app*
```
mkdir dashboard/templates
```
**Step 12** - *Create another directory inside templates with the same name of the app*
```
mkdir dashboard/templates/dashboard
```
**Step 13** - *Create index.html*
**Step 14** - *In views.py define the index view*
``` python
def index(request):
    render(request, "dashboard/index.html")

def jobs(request):
    render(request, "dashboard_jobs/jobs.html")
```
**Step 15** - *From django project copy urls.py to your app folder*
**Step 16** - *Import your views and create your paths*
``` python
# Should look like this
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('jobs/dashboard', views.dashboard_jobs, name='index'),
]
```
NOTE: inside the urls.py is an guide for how to add urls, check it.
**Step 16** - *Include 'dashboard.urls' in django project folder*
``` python
# Should look like this
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('dashboard.urls')),
]
```
**Step 17** - *Run the server*