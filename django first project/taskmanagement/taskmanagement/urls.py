"""
URL configuration for taskmanagement project.

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
from django.contrib import admin
from django.urls import path
from task import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('task-list/',views.task_list,name='task-list'),
    path('task-create/',views.task_create,name='task-create'),
    path('task-detail/<int:pk>/',views.task_detail,name='task-detail'),
    path('task-update/<int:pk>/',views.task_update,name='task-update'),
    path('task-delete/<int:pk>/',views.task_delete,name='task-delete'),
    path('login/',views.login_page,name='login-page'),
    path('register/',views.register,name='register'),
    path('logout',views.logout_page,name="logout")
]
