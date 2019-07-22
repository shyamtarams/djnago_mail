from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.conf import settings  
  
def setcookie(request):  
    response = HttpResponse("Cookie Set")  
    response.set_cookie('java-tutorial', 'javatpoint.com')  
    return response  
def getcookie(request):  
    tutorial  = request.COOKIES['java-tutorial']  
    return HttpResponse("java tutorials @: "+  tutorial);  
