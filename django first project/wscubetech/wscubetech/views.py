from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,redirect
from .forms import usersForm
from service.models import service

def homePage(request):
    servicesData = service.objects.all()
    data = {
        'servicesData':servicesData
    }
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
    return render(request,"index2.html",data)

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
            n3 = int(request.POST.get('num3'))
            finalans = n1+n2+n3
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
    fn = usersForm()
    # data={}
    data = {'form':fn}
    try:
        # if request.method == "GET":
        if request.method == "POST":
        # n1 = int(request.GET['num1'])
        # n2 = int(request.GET['num2'])
            # n1 = int(request.GET.get('num1'))
            # n2 = int(request.GET.get('num2'))
            n1 = int(request.POST.get('num1'))
            n2 = int(request.POST.get('num2'))
            n3 = int(request.POST.get('num3'))
            finalans = n1+n2+n3
            data = {
                # 'n1':n1,
                # 'n2':n2,
                'form':fn,
                'output':finalans
            }
            url = "/thankyou/?output={}".format(finalans)
            # return HttpResponseRedirect(url)
            return redirect(url)
    except:
        pass
    return render(request,"userform.html",data)

def calculator(request):
    c=''
    try:
        if request.method == "POST":
            n1 = eval(request.POST.get('num1'))
            n2 = eval(request.POST.get('num2'))
            opr = request.POST.get('opr')
            if opr=="+":
                c = n1 + n2
            elif opr == "-":
                c = n1 - n2
            elif opr == "*":
                c = n1*n2
            elif opr == "/":
                c = n1/n2
            
    except:
        c = "invalid opr.."
    return render(request,"calculator.html",{'c':c})

def saveevenodd(request):
    c=''
    if request.method == "POST":
        if request.POST.get('num1') == "":
            return render(request,"even-odd.html",{'error':True})
        n = eval(request.POST.get('num1'))
        if n%2==0:
            c = "Even Number"
        else:
            c = "Odd Number"
    return render(request,"even-odd.html",{'c':c})

def marksheet(request):
    data={}
    if request.method == "POST":
        s1 = eval(request.POST.get('subject1'))
        s2 = eval(request.POST.get('subject2'))
        s3 = eval(request.POST.get('subject3'))
        s4 = eval(request.POST.get('subject4'))
        s5 = eval(request.POST.get('subject5'))
        t=s1+s2+s3+s4+s5
        p = t*100/500
        if p>=60:
            d="first Div"
        elif p>=48:
            d="second div"
        elif p>=35:
            d="third div"
        else:
            d="fourth div"
        data={
            'total':t,
            'per':p,
            'div':d
        }
    return render(request,"marksheet.html",data)