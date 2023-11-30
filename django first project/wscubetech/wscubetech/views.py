from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,redirect

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
    return render(request,"index2.html")

def submitForm(request):
    finalans = 0
    data={}
    try:
        # if request.method == "GET":
        if request.method == "POST":
        # n1 = int(request.GET['num1'])
        # n2 = int(request.GET['num2'])
            # n1 = int(request.GET.get('num1'))
            # n2 = int(request.GET.get('num2'))
            n1 = int(request.POST.get('num1'))
            n2 = int(request.POST.get('num2'))
            finalans = n1+n2
            data = {
                'n1':n1,
                'n2':n2,
                'output':finalans
            }

            return HttpResponse(finalans)
    except:
        pass

def aboutUS(request):
    return render(request,"index1.html")

def contactUs(request):
    return render(request,"contact.html")

def priceUs(request):
    return render(request,"pricing.html")

def downloadUs(request):
    return render(request,"download.html")

def course(request):
    return HttpResponse("Learning about Django")

def courseDetails(request,courseid):
    return HttpResponse(courseid)

def courseDetails(request,courseid):
    return HttpResponse(courseid)

def thankyou(request):
    if request.method == "GET":
        output = request.GET.get('output')
    return render(request,"thank-you.html",{'output':output})

def userForm(request):
    finalans = 0
    data={}
    try:
        # if request.method == "GET":
        if request.method == "POST":
        # n1 = int(request.GET['num1'])
        # n2 = int(request.GET['num2'])
            # n1 = int(request.GET.get('num1'))
            # n2 = int(request.GET.get('num2'))
            n1 = int(request.POST.get('num1'))
            n2 = int(request.POST.get('num2'))
            finalans = n1+n2
            data = {
                'n1':n1,
                'n2':n2,
                'output':finalans
            }
            url = "/thankyou/?output={}".format(finalans)
            # return HttpResponseRedirect(url)
            return redirect(url)
    except:
        pass
    return render(request,"userform.html",data)