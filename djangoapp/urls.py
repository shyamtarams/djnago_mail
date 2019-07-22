from django.urls import path
#from convert_to_pdf import views
#from sessionapp import views
#from cookiesapp import views
#from validateapp import views
from djangoapp import views



urlpatterns = [
     #path('djangoapp', views.mail.as_view()),
     path('mail/',views.mail),
     #path('pdf',views.getpdf),  
     #path('index/', views.issessionndex),  
     #path('scookie',views.setcookie),  
     #path('gcookie',views.getcookie),
    
     #path('ssession',views.setsession),  
     #path('gsession',views.getsession),
     #path('index',views.index),

  
     


       
]
