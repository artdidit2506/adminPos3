from django.shortcuts import render


# Create your views here.


def contactindex(request):
    return render(request, 'contact/contactindex.html')
