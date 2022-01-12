from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


# Create your views here.

def login(request: HttpRequest):
    return render(request, "accounts/login.html", {})
