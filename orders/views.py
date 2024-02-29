from django.shortcuts import render


def show(request):
    return render(request, 'show.html')


def checkout(request):
    return render(request, 'checkout.html')
