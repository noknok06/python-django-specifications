# manager/views.py

from django.shortcuts import render

def manager_home(request):
    return render(request, 'manager/manager_home.html')
