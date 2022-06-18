from multiprocessing import context
from django.shortcuts import render
def home(request):
    context = {'home':'active'}
    return render(request, 'home.html',context)

def contact(request):
    context = {'contact':'active'}
    return render(request,'contact.html',context)
