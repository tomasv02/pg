from django.http import HttpResponse

def homepage(request):
    return HttpResponse("Test lorem ipsum")

def about(request):
    return HttpResponse("2Test lorem ipsum2")
