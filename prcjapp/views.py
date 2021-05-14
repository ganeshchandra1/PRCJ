from django.shortcuts import render
from django.http import HttpResponse
import re
from django.utils.timezone import datetime

# Create your views here.
def home(request):
    return HttpResponse("Hello, Django!")

def prac(request):
    time=datetime.now()
    name="ram"
    formatted=time.strftime("%A,%d %B, %Y at %X")
    match_obj=re.match("[A-Za-z]+",name)
    if match_obj:
        cleanname=match_obj.group(0)

    else:
        cleanname="failed"
        
    return HttpResponse(cleanname)