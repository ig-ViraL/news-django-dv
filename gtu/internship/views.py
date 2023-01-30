from http.client import responses
from tarfile import RECORDSIZE
from django.shortcuts import render
import requests

# Create your views here.
def index(request):
    records = {}
    url="https://inshortsapi.vercel.app/news?category="
    response = requests.get(url=url)
    data = response.json()
    records['data'] = data
    return render(request,'index.html',records)

def sports(request):
    records = {}
    url="https://inshortsapi.vercel.app/news?category=sports"
    response = requests.get(url=url)
    data = response.json()
    records['data'] = data
    return render(request,'sports.html',records)

def business(request):
    records = {}
    url="https://inshortsapi.vercel.app/news?category=business"
    response = requests.get(url=url)
    data = response.json()
    records['data'] = data
    return render(request,'business.html',records)

def entertainment(request):
    records = {}
    url="https://inshortsapi.vercel.app/news?category=entertainment"
    response = requests.get(url=url)
    data = response.json()
    records['data'] = data
    return render(request,'entertainment.html',records)

def national(request):
    records = {}
    url="https://inshortsapi.vercel.app/news?category=national"
    response = requests.get(url=url)
    data = response.json()
    records['data'] = data
    return render(request,'national.html',records)

def world(request):
    records = {}
    url="https://inshortsapi.vercel.app/news?category=world"
    response = requests.get(url=url)
    data = response.json()
    records['data'] = data
    return render(request,'world.html',records)

def politics(request):
    records = {}
    url="https://inshortsapi.vercel.app/news?category=politics"
    response = requests.get(url=url)
    data = response.json()
    records['data'] = data
    return render(request,'politics.html',records)

def technology(request):
    records = {}
    url="https://inshortsapi.vercel.app/news?category=technology"
    response = requests.get(url=url)
    data = response.json()
    records['data'] = data
    return render(request,'technology.html',records)

def startup(request):
    records = {}
    url="https://inshortsapi.vercel.app/news?category=startup"
    response = requests.get(url=url)
    data = response.json()
    records['data'] = data
    return render(request,'startup.html',records)

def miscellaneous(request):
    records = {}
    url="https://inshortsapi.vercel.app/news?category=miscellaneous"
    response = requests.get(url=url)
    data = response.json()
    records['data'] = data
    return render(request,'miscellaneous.html',records)

def science(request):
    records = {}
    url="https://inshortsapi.vercel.app/news?category=science"
    response = requests.get(url=url)
    data = response.json()
    records['data'] = data
    return render(request,'science.html',records)

def automobile(request):
    records = {}
    url="https://inshortsapi.vercel.app/news?category=automobile"
    response = requests.get(url=url)
    data = response.json()
    records['data'] = data
    return render(request,'automobile.html',records)    

def about(request):
    return render(request,'about.html')