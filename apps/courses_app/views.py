from django.shortcuts import render, redirect
from datetime import datetime
# Create your views here.
def index(request):
    return render(request,'courses_app/index.html')