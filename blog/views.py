from django.shortcuts import render
from .models import post_list
from bs4 import BeautifulSoup as bs
import requests

def home(request):
    links = [x['url'] for x in post_list.objects.all().values()]
    titles = []
    images = []
    for link in links:
        page = requests.get(link)
        soup = bs(page.text, 'html.parser')
        titles.append(soup.find('title').text)
        images.append(soup.find('div', {'id' : 'readme'}).find('img')['src'])
    context = {'posts' : zip(titles, links, images)}
    return render(request, 't.html', context)
