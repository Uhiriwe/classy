from django.shortcuts import render
from .models import classy

# Create your views here.
def index(request):
    getAllPosts = classy.objects.all()
    return render(request, 'index.html', { 'getAllPosts': getAllPosts })
def new_design(request):
    return render(request, 'new_fashion.html', {})

def talk_to_us(request):
    return render(request, 'talk_to_us.html', {})