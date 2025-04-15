from django.shortcuts import render

def homepage(request):
   return render(request, 'main.html') #zavolá main html stranku

def print(request):
    return render(request, 'print.html') #volání podstranky print
