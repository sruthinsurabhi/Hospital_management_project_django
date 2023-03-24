from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    person=[{'name':'Jack',
             'age':55,
             'place':"Caribean"},{'name':'Sparrow',
             'age':25,
             'place':"Caribean"},{'name':'gibbs',
             'age':65,
             'place':"gulf"}]
    context = {'person': person}
    return render(request,'index.html',context)

def about(request):
    return render(request,'about.html')
def booking(request):
    return render(request,'booking.html')
def doctors(request):
    return render(request,'doctors.html')
def contact(request):
    return render(request,'contact.html')
def department(request):
    return render(request,'department.html')

