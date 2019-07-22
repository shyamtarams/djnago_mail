from django.shortcuts import render

# Create your views here.
from django.conf import settings  
#from validateapp.form import EmployeeForm  

def emp(request):  
    if request.method == "POST":  
       form = EmployeeForm(request.POST)  
       if form.is_valid():  
          try:  
             return redirect('/')  
          except:  
                pass  
    else:  
        form = EmployeeForm()  
    return render(request,'index.html',{'form':form})  
