from django.shortcuts import render

# Create your views here.


from django.http import HttpResponse
from subprocess import call, Popen



def index(request):
    Popen(["git", "pull"],
          cwd="/home/ferrelucas/workspace/alura-site").wait()
    Popen(["python2.7", "/home/ferrelucas/workspace/google-cloud-sdk/platform/google_appengine/appcfg.py", "update", "."],
          cwd="/home/ferrelucas/workspace/alura-site").wait()
    return HttpResponse("Deployment completed!")