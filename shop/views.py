from django.shortcuts import render
from django.http import HttpResponse
from .models import Products


def main_page(request):
    atall = Products.objects.all()
    return render(request, 'mother.html', {'Products': atall})
