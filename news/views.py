from django.shortcuts import render
from .models import News

def index(request):
    news_list = News.objects.all()[:2]
    context = {'news': news_list}
    return render(request, 'news/base_news.html', context)

