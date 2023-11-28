from django.http import HttpResponse

def aboutUS(request):
    return HttpResponse("Welcome to wscubetech")

def course(request):
    return HttpResponse("Learning about Django")

def courseDetails(request,courseid):
    return HttpResponse(courseid)