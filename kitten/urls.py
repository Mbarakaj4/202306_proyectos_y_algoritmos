"""
URL configuration for kitten app.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views, auth

urlpatterns = [
    path('', views.index, name='index'),
    path('auth/', auth.auth, name='auth'),
    path('register/', auth.register, name='register'),
    path('logout/', auth.logout, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('dashboard/clients/', views.clients, name='clients'),
    path('dashboard/orders/', views.orders, name='orders'),
    path('dashboard/clients/add/', views.add_client, name='add_client'),
    path('dashboard/clients/edit/<int:client_id>', views.edit_client, name='edit_client'),
    path('dashboard/clients/delete/<int:client_id>', views.delete_client, name='delete_client'),
    path('dashboard/clients/view/<int:client_id>', views.view_client, name='view_client'),
    path('workorders/', views.workorders, name='workorders'),
    path('workorders/details/<int:workorder_id>/', views.workorders_details, name='workorders_details'),
]
