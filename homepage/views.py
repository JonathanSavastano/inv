from django.shortcuts import render
from .models import Computer

# Create your views here.
def home(request):
    return render(request, 'homepage/home.html')

def inventory(request):
    computers = Computer.objects.all() # fetch all computers
    return render(request, 'homepage/inventory.html', {'computers': computers})