from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.




def home(request):
    # return HttpResponse('Hello there friend!')
    return render(request, 'generator/home.html')  # Needs to be able to find home.html


def about(request):
    return render(request, 'generator/about.html')


def password(request):

    characters = list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get('uppercase'):  # inside get() variable needs to match html form
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('special'):
        characters.extend(list("!@##$%^&*()"))
    if request.GET.get('numbers'):
        characters.extend(list("1234567890"))

    length = int(request.GET.get("length", 12))  # requestrequest.GET.get() will get the variables you created in the password generator form

    thepassword = ""

    for x in range(length):
        thepassword += random.choice(characters)

    return render(request, 'generator/password.html', {"password": thepassword})
