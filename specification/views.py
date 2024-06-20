# specification/views.py

from django.shortcuts import render

def specification_home(request):
    return render(request, 'specification/specification_home.html')
