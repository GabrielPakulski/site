from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'name': 'Gabriel Pakulski'
    }
    return render(request, 'index.html', context)

def contact(request):
    context = {
        'name': 'Gabriel Pakulski',
        'phone': '+55 51 999 577 691',
        'email': 'gabrielpakulski@hotmail.com'
    }
    return render(request, 'contact.html')