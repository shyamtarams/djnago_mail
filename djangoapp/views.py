from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse  
#from djangoapp import settings  
from django.conf import settings
from django.core.mail import send_mail  
  
  
def mail(request):  
    subject = "hi santhosh"  
    msg     = "Congratulations for your success"  
    email_from = "settings.EMAIL_HOST_USER"
    to      = "santhoshk728@gmail.com"  
    #res     = send_mail(subject, msg, settings.EMAIL_HOST_USER, [to]) 
    res     = send_mail(subject, msg, email_from, [to])  
    if(res == 1):  
        msg = "Mail Sent Successfuly"  
    else:  
        msg = "Mail could not sent"  
    return HttpResponse(msg)
