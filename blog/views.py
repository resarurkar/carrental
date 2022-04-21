from multiprocessing import context
from django.shortcuts import render
from .models import Post

posts = [
    {
        'author': 'Sudha Murthey',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted' : 'April 13, 2022'
    },
    {
        'author': 'Jordan peterson',
        'title': 'Blog Post 2',
        'content': 'second post content',
        'date_posted' : 'April 15, 2022'
    }

]


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render (request, 'blog/home.html', context)

def about(request):
    return render (request, 'blog/about.html', {'title' : 'About'})

# Create your views here.
