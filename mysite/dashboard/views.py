from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Category, News, Authors, Reference
from .forms import CategoryForm, NewsForm, AuthorsForm, ReferenceForm
from . import servise


def login_required_decorator(f):
    return login_required(f, login_url="login")


@login_required_decorator
def dashboard_page(request):
    categories = servise.news_count()
    views = servise.get_view()
    cat_count = servise.get_category_count()
    aut_count = servise.get_author_count()
    ref_count = servise.get_ref()
    new_count = servise.get_news_count()
    ctx = {
        'categories': categories,
        'views': views,
        'cat_count': cat_count,
        'aut_count': aut_count,
        'ref_count': ref_count,
        'new_count': new_count,
    }
    return render(request, 'dashboard/index.html', ctx)


def dashboard_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
    return render(request, 'dashboard/login.html')


def dashboard_logout(request):
    logout(request)
    return redirect('login')


def category_list(request):
    categories = servise.get_categories()
    count = servise.news_count()
    print(count)
    ctx = {
        "categories": categories
    }
    return render(request, 'dashboard/category/list.html', ctx)


def category_create(request):
    model = Category()
    form = CategoryForm(request.POST, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('category_list')
        else:
            print(form.errors)
    ctx = {
        "form": form
    }
    return render(request, 'dashboard/category/form.html', ctx)


def category_edit(request, pk):
    model = Category.objects.get(id=pk)
    form = CategoryForm(request.POST or None, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('category_list')
        else:
            print(form.errors)
    ctx = {
        "form": form
    }
    return render(request, 'dashboard/category/form.html', ctx)


def category_delete(request, pk):
    model = Category.objects.get(pk=pk)
    model.delete()
    return redirect('category_list')


def author_list(request):
    authors = servise.get_author()
    ctx = {
        "authors": authors
    }
    return render(request, 'dashboard/author/list.html', ctx)


def author_create(request):
    model = Authors()
    form = AuthorsForm(request.POST, request.FILES, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('author_list')
        else:
            print(form.errors)
    ctx = {
        "form": form
    }
    return render(request, 'dashboard/author/form.html', ctx)


def author_edit(request, pk):
    model = Authors.objects.get(id=pk)
    form = AuthorsForm(request.POST or None, request.FILES, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('author_list')
        else:
            print(form.errors)
    ctx = {
        "form": form
    }
    return render(request, 'dashboard/author/form.html', ctx)


def author_delete(request, pk):
    model = Authors.objects.get(id=pk)
    model.delete()
    return redirect('author_list')


def news_list(request):
    news = servise.get_news()

    ctx = {
        "news": news
    }
    return render(request, 'dashboard/news/list.html', ctx)


def news_create(request):
    model = News()
    form = NewsForm(request.POST, request.FILES, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('news_list')
        else:
            print(form.errors)
    ctx = {
        "form": form
    }
    return render(request, 'dashboard/news/form.html', ctx)


def news_edit(request, pk):
    model = News.objects.get(id=pk)
    form = NewsForm(request.POST or None, request.FILES, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('news_list')
        else:
            print(form.errors)
    ctx = {
        "form": form
    }
    return render(request, 'dashboard/news/form.html', ctx)


def news_delete(request, pk):
    model = News.objects.get(id=pk)
    model.delete()
    return redirect('news_list')


def reference_list(request):
    references = Reference.objects.all()
    ctx = {
        "references": references
    }
    return render(request, 'dashboard/reference/list.html', ctx)


def reference_create(request):
    model = Reference()
    form = ReferenceForm(request.POST, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('reference_list')
        else:
            print(form.errors)
    ctx = {
        "form": form
    }
    return render(request, 'dashboard/reference/form.html', ctx)


def reference_edit(request, pk):
    model = Reference.objects.get(id=pk)
    form = ReferenceForm(request.POST or None, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('reference_list')
        else:
            print(form.errors)
    ctx = {
        "form": form
    }
    return render(request, 'dashboard/reference/form,html', ctx)


def reference_delete(request, pk):
    model = Reference.objects.get(id=pk)
    model.delete()
    return redirect('reference_list')
