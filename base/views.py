from django.shortcuts import render

# Create your views here.
def basehome(request):
    return render(request, 'base/basehome.html')