from django.shortcuts import render
from django.contrib.auth.hashers import make_password, check_password
from .models import Users
from django.http import HttpResponseRedirect

def index(request):
    return render(request, 'analysietta/index.html')

def register(request):
    if request.method == "POST":
        obj = Users()
        obj.email = request.POST["email"]
        obj.password = make_password(request.POST["password"])
        obj.save()
        #return HttpResponseRedirect('register')

def check(request):
    if request.method == "POST":
        print(Users.objects.all())
