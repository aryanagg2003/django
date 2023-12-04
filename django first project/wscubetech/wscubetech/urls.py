"""
URL configuration for wscubetech project.

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
from wscubetech import views

urlpatterns = [
    path('admin-panel/', admin.site.urls),
    path('', views.homePage),
    path('about-us/',views.aboutUS),
    path('contact-us/',views.contactUs,name="contact"),
    path('price-us/',views.priceUs,name="price"),
    path('download/',views.downloadUs,name="download"),
    path('course/',views.course),
    path('thankyou/',views.thankyou),
    path('submitfrom/',views.submitForm,name="submitform"),
    path('calculator/',views.calculator),
    path('saveevenodd/',views.saveevenodd,name="saveevenodd"),
    path('marksheet/',views.marksheet),
    path('course/<int:courseid>',views.courseDetails),
    path('userform/',views.userForm),
    path('newsdetails/<id>',views.newsDetails),
]
