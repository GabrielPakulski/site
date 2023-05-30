from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

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

def error404(request, e):
    template = loader.get_template('404.html')
    return HttpResponse(content=template.render(), content_type='text/html; charset=utf8', status=404)