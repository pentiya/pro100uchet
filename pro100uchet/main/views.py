from django.shortcuts import render

# Create your views here.

def index(request):
#    return HttpResponse("Hello, world. You're at the polls index.")
    return render(request, 'main/index.html')

def map(request):
#    return HttpResponse("Hello, world. You're at the polls index.")
    return render(request, 'main/map.html')
