from django.shortcuts import render

# Create your views here.
def adminweb(request):
    return render(request, 'adminweb/adminweb.html')