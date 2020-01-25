from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

def home(request):
    return render(request, "main/homepage.html")
