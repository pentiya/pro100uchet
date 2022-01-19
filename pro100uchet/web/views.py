from django.shortcuts import render

# Create your views here.

def web_index(request):
#    return HttpResponse("Hello, world. You're at the polls index.")
    return render(request, 'web/web-index.html')

def map_index(request):
#    return HttpResponse("Hello, world. You're at the polls index.")
    return render(request, 'web/web-map.html')
