from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author' : 'Roshan Mehta',
        'title' : 'Django Learning',
        'content' : 'First post content', 
        'Date' : 'Dec 9, 2020'
    },
    {
        'author' : 'My Shizu',
        'title' : 'Django Learning',
        'content' : 'Second post content', 
        'Date' : 'Dec 9, 2020'
    }

]

def home(request):
    context = {
        'posts' : posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    title = "About"
    return render(request, 'blog/about.html', {"title" : title})