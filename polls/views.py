from django.shortcuts import render

# Create your views here.


from django.http import HttpResponse
from subprocess import call



def index(request):
    call(["git", "clone", "git@github.com:BLIMBA.git"])
    return HttpResponse("Hello, world. You're at the polls index.")