from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    context = {'welcome_msg': "This message is by context."}
    return render(request, "standalone/home.html", context) 
