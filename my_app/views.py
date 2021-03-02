from django.shortcuts import render
from bs4 import BeautifulSoup
import requests
# Create your views here.
def home(request):
    return render(request, template_name='base.html')

def new_search(request):
    search = request.POST.get('search')
    print(search)
    stuff_for_frontend = {
        'search' : search,
        'bibi' : 'bibixx'
    }
    return render(request,  'my_app/new_search.html', stuff_for_frontend)