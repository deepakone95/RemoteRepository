from django.shortcuts import render
def home_page(request):
    return render(request,'home.html')

def registration_page(request):
    return render(request,'registration.html')

def services_page(request):
    return render(request,'services.html')

def feedback_page(request):
    return render(request,'feedback.html')

def gallery_page(request):
    return render(request,'gallery.html')