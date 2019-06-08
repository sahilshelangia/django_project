from django.shortcuts import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("<h1 style='text-align:center;padding-top:100px;'>Coming Soon</h1>")