from django.shortcuts import render
from .models import News
from django.http import Http404

def index(request):
    news_list = News.objects.all()[:2]
    context = {'news': news_list}
    return render(request, 'news/base_news.html', context)
