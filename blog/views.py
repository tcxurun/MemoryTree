# coding:utf-8
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from blog.models import Article, Category
import calendar, datetime
from django.contrib.syndication.views import Feed

# Create your views here.
def index(request):
    """首页"""
    archive_dates = Article.objects.datetimes('publish_date', 'month', order='ASC')
    categories = Category.objects.all()

    page = request.GET.get('page')
    article_queryset = Article.objects.all().order_by('-publish_date')
    paginator = Paginator(article_queryset, 5,)

    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
        #  如果page不是一个整数,返回第一页
        articles = paginator.page(1)
    except EmptyPage:
        #  如果页数超过边界,返回最后一页
        articles = paginator(paginator.num_pages)

    return render(
        request,
        "blog/index.html",
        {
            "articles": articles,
            "archive_dates": archive_dates,
            "categories": categories
        })

def detail(request, id):
    """文章详情页面"""
    article = get_object_or_404(Article, id = str(id))
    archive_dates = Article.objects.datetimes('publish_date', 'month', order='DESC')
    categories = Category.objects.all()
    return render(
        request,
        "blog/detail.html",
        {
            "article": article,
            "archive_dates": archive_dates,
            "categories": categories
        })

def date_archive(request, year, month):
    """根据所选日期选择文章"""
    year = int(year)
    month = int(month)
    month_range = calendar.monthrange(year, month)
    start = datetime.datetime(year=year, month=month, day=1)
    end = datetime.datetime(year=year, month=month, day=month_range[1])
    archive_dates = Article.objects.datetimes('publish_date', 'month', order='DESC')
    categories = Category.objects.all()

    page = request.GET.get('page')
    article_queryset = Article.objects.filter(publish_date__range = (start.date(), end.date()))
    paginator = Paginator(article_queryset, 5,)

    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
        #  如果page不是一个整数,返回第一页
        articles = paginator.page(1)
    except EmptyPage:
        #  如果页数超过边界,返回最后一页
        articles = paginator(paginator.num_pages)

    return render(
        request,
        "blog/date_archive.html",
        {
            "start": start,
            "end": end,
            "articles": articles,
            "archive_dates": archive_dates,
            "categories": categories
        })

def category_archive(request, id):
    archive_dates = Article.objects.datetimes('publish_date', 'month', order='DESC')
    categories = Category.objects.all()
    category = get_object_or_404(Category, id=str(id))

    page = request.GET.get('page')
    article_queryset = Article.objects.filter(categories = category)
    paginator = Paginator(article_queryset, 5,)

    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
        #  如果page不是一个整数,返回第一页
        articles = paginator.page(1)
    except EmptyPage:
        #  如果页数超过边界,返回最后一页
        articles = paginator(paginator.num_pages)

    return render(
        request,
        "blog/category_archive.html",
        {
            "articles": articles,
            "archive_dates": archive_dates,
            "categories": categories,
            "categories": categories
        })

def about_me(request):
    return render(request, "blog/aboutme.html")

class RSSFeed(Feed):
    title = "RSS feed - article"
    link = "feed/articles"
    description = "RSS feed - blog articles"

    def item(self):
        return Article.objects.order_by("-publish_date")

    def item_title(self, item):
        return item.title

    def item_publish_date(self, item):
        return item.publish_date

    def item_description(self, item):
        return item.content
