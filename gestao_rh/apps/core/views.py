from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required()
def inicio(request):
    return render(request, 'core/index.html')

def saiu(request):
    return render(request, 'registration/logged_out.html')