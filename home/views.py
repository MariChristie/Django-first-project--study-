from django.shortcuts import render
from django.http import HttpResponse
from .models import User

def home(request):
    if request.method == "GET":
        return render (request, 'home.html')
    else:
        name = request.POST.get('name')

        User = User(
            name=name
        )

        User.save()
        return HttpResponse(name)