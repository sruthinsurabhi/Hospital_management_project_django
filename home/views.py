from django.http import HttpResponse
from django.shortcuts import render
from.models import departments, doctors
from .forms import BookingForm

# Create your views here.
def index(request):
  
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')
def booking(request):
    if request.method =="POST":
        
        form=BookingForm(request.POST)
        if form.is_valid():
            form.save()
            dict_form={'form':form,
                       }
            return render(request,'confirmation.html',dict_form)
        
    form=BookingForm()
    dict_form={'form':form,}
    return render(request,'booking.html',dict_form)

def doctor(request):
    dict_doc = {
        'doct':doctors.objects.all()
        }

    return render(request,'doctors.html',dict_doc)

def contact(request):
    return render(request,'contact.html')
   

def department(request):
    dict_dept={'Dept':departments.objects.all()}

    return render(request,'department.html',dict_dept)

