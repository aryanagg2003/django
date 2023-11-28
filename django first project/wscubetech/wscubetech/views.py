from django.http import HttpResponse
from django.shortcuts import render

def homePage(request):
    # data = {
    #     'title':'Home Page',
    #     'bdata':'Welcome to wscubetech',
    #     'clist':['C++','Python','Django'],
    #     'numbers':[10,20,30,40,50],
    #     'student_details' : [
    #         {'name':'pradeep','phone':1232355287},
    #         {'name':'testing','phone':1232355287}
    #     ]
    # }
    return render(request,"index.html")

def aboutUS(request):
    return HttpResponse("Welcome to wscubetech")

def course(request):
    return HttpResponse("Learning about Django")

def courseDetails(request,courseid):
    return HttpResponse(courseid)