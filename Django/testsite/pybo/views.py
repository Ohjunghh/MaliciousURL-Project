from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("감자튀김")
# Create your views here.
