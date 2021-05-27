import datetime

from django.shortcuts import render, get_list_or_404, get_object_or_404, redirect
from dashboard.models import *
from django.utils import timezone
import datetime


def index(request):
    authors = Authors.objects.all()
    actuals = News.objects.all().filter(
       created_at__range=[timezone.now() - datetime.timedelta(days=1), timezone.now()]
    )
    populars = News.objects.all().order_by("-views")[:4]
    fresh_news = News.objects.all().order_by("-created_at")[:4]
    categories = Category.objects.all()
    policies = News.objects.all().filter(category_id=2)
    cultures = News.objects.all().filter(category_id=4)
    al = News.objects.all().filter(category_id=3)
    sports = News.objects.all().filter(category_id=5)
    worlds = News.objects.all().filter(category_id=6)
    weathers = News.objects.all().filter(category_id=7)
    economics = News.objects.all().filter(category_id=1)
    sums = News.objects.all()
    ctx = {
        "actuals": actuals,
        "authors": authors,
        "populars": populars,
        "fresh_news": fresh_news,
        "categories": categories,
        "policies": policies,
        "economics": economics,
        "cultures": cultures,
        "al": al,
        "sums": sums,
        "sports": sports,
        "worlds": worlds,
        "weathers": weathers,
    }
    return render(request, 'fronted/news/index.html', ctx)


def contact(request):
    categories = Category.objects.all()
    reference = Reference()
    if request.POST:
        reference.name = request.POST.get("name")
        reference.email = request.POST.get("email")
        reference.message = request.POST.get("message")
        reference.save()
    ctx = {
        "categories": categories
    }
    return render(request, 'fronted/news/contact.html', ctx)


def category(request, category_id=None):
    categories = Category.objects.all()[:7]
    news = News.objects.all().filter(category_id=category_id)
    new = news[0]
    new1 = news[1:]
    sums = News.objects.all()
    ctx = {
        "categories": categories,
        "new": new,
        "new1": new1,
        "news": news,
        "sums": sums

    }
    return render(request, 'fronted/news/category.html', ctx)


def view(request, news_id=None):
    categories = Category.objects.all()
    new = News.objects.get(id=news_id)
    print(new)
    new.views = new.views + 1
    new.save()
    print(new.views)
    sums = News.objects.all().order_by("-views")

    ctx = {
        "new": new,
        "sums": sums,
        "categories": categories
    }
    return render(request, 'fronted/news/view.html', ctx)


def search(request):
    news = []
    fresh_news = News.objects.all().order_by("-created_at")
    if request.GET and request.GET.get("search"):
        news = News.objects.filter(title__icontains=request.GET.get("search"))
        print("Search", news)
    ctx = {
        "news": news,
        "fresh_news": fresh_news,
        "search_count": len(news),
        "search_text": request.GET.get("search")
    }
    return render(request, "fronted/news/search.html", ctx)
