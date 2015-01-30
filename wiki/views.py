# coding:utf-8
from django.shortcuts import render, get_object_or_404, render_to_response
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from wiki.models import Post, Category

# Create your views here.
def index(request):
    """首页"""
    categories = Category.objects.filter(parent = None)

    page = request.GET.get('page')
    post_queryset = Post.objects.all().order_by('-publish_date')
    paginator = Paginator(post_queryset, 5,)

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        #  如果page不是一个整数,返回第一页
        posts = paginator.page(1)
    except EmptyPage:
        #  如果页数超过边界,返回最后一页
        posts = paginator(paginator.num_pages)

    return render(
        request,
        "wiki/index.html",
        {
            "posts": posts,
            "categories": categories
        })

def single(request, id):
    """文章详情页面"""
    post = get_object_or_404(Post, id = str(id))
    categories = Category.objects.all()
    return render(
        request,
        "wiki/single.html",
        {
            "post": post,
            "categories": categories
        })

def category_archive(request, id):
    categories = Category.objects.all()
    category = get_object_or_404(Category, id=str(id))

    page = request.GET.get('page')
    post_queryset = Post.objects.filter(categories = category)
    paginator = Paginator(post_queryset, 5,)

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        #  如果page不是一个整数,返回第一页
        posts = paginator.page(1)
    except EmptyPage:
        #  如果页数超过边界,返回最后一页
        posts = paginator(paginator.num_pages)

    return render(
        request,
        "wiki/category_archive.html",
        {
            "posts": posts,
            "categories": categories,
            'category': category
        })

def category_view(request):
    cates = Category.objects.all()
    for cate in cates:
        print 'title: %s' % cate.title
    return render_to_response(
        'wiki/category.html',
        {
            'nodes': cates,
        }
    )
