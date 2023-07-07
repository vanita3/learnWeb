from django.shortcuts import render

# Create your views here.
#def index(request):
 #   return render(request,'firstApp/home.html')

def home(request):
    return render(request,'firstApp/home.html')

def base(request):
    return render(request,'firstApp/base.html')

def about(request):
    return render(request,'firstApp/about1.html')

def contact(request):
    return render(request, 'firstApp/contact.html')

def portfolio(request):
    return render(request, 'firstApp/portfolio.html')

def services(request):
    return render(request,'firstApp/services.html')

