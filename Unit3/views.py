from django.shortcuts import render

def home(request):
    context = {
        'title': 'Homepage',
        'message': 'Welcome to the Homepage!'
    }
    return render(request, 'Unit3/home.html', context)

def blog(request):
    context = {
        'title': 'Blogpage',
        'message': 'Welcome to the Blogpage!'
    }
    return render(request, 'Unit3/blog/blog.html', context)
