from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def Contact(request):
    return render(request, 'Contact.html')

def Gallery(request):
    return render(request, 'Gallery.html')

def Recovery(request):
    return render(request, 'Recovery.html')

def Service(request):
    return render(request, 'Service.html')

def Team(request):
    return render(request, 'Team.html')