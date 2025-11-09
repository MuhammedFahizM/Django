from django.http import HttpResponse

def Home(request):
    return HttpResponse("Hello,this is middleware example!")
