from datetime import timezone
from django.shortcuts import render
def home(request):
    return render(request,'home.html')
def about(request):
    return render(request,'about.html')
def work(request):
    return render(request,'work.html')
def Contact(request):
    if request.method=="POST":
        name=request.POST.GET('name')
        mobile=request.POST.GET('mobile')
        email=request.POST.GET('email')
        feedback=request.POST.GET('feedback')
        contact=Contact(name=name,mobile=mobile,email=email,feedback=feedback)
        contact.save()
    return render(request,'contact.html')

def about(request):
    return render(request,'about.html')




