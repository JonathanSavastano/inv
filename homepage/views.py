from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'homepage/home.html')

def inventory(request):
    return render(request, 'homepage/inventory.html')