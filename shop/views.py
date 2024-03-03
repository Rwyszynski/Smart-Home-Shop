from django.shortcuts import render
from django.http import HttpResponse
from .models import Products


def main_page(request):
    atall = Products.objects.all()
    return render(request, 'main.html', {'Products': atall})

# Brakuje kodu by pokażywać wsztkie info o produkcie


def about(request):
    return render(request, 'about.html')


def shop(request):
    return render(request, 'shop.html')


def contact(request):
    return render(request, 'contact.html')
