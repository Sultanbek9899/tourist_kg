from unicodedata import category
from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
# Create your views here.

from post.models import Post, Category, Comment
from post.forms import CommentForm

def index(request):
    posts=Post.objects.all()
    categories = Category.objects.all()
    context = {
        "posts":posts,
        "categories":categories
    }
    return render(request, 'index.html', context=context)


def get_post_list(request, slug=None):
    if slug is not None:
        posts = Post.objects.filter(category__slug=slug, is_active=True)
    else:
        posts = Post.objects.filter(is_active=True)
    context = {
        "posts":posts,
    }
    return render(request, "post_list.html", context=context)



def get_post_detail(request, pk):
    try: #Пытаемся найти пост по id, если нет. То выводим 404 ошибку
        post=Post.objects.get(id=pk) #используем get для получени
        comments = Comment.objects.filter(post=post)
    except Post.DoesNotExist:
        raise Http404()
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.post = post
            instance.save()
        return redirect("post_detail", pk=post.id)
    else:
        form = CommentForm()
    
    context = {     # одного объекта класса Post
        "post":post,
        "form":form,
        "comments":comments
    }    


    return render(request, 'post_detail.html', context)
