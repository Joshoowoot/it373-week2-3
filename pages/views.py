from django.shortcuts import render
from pages.models import Post

# Create your views here.
def home(request):
    context = {
        'title': 'Home Page', 'features': ['Django', 'Templates', 'Static Files']
    }
    return render(request, 'home.html', context)

def about(request):
    return render(request, 'about.html', {'title': 'About Page'})

def hello(request, name):
    return render(request, 'hello.html', {'name': name})

def gallery(request):
    images = [
        'img1.jpg',
        'img2.jpg',
        'img3.jpg',
    ]
    return render(request, 'gallery.html', {'images': images})

def page_not_found_view(request, exception):
    return render(request, '404.html', status=404)

def server_error_view(request):
    return render(request, '500.html', status=500)

def posts_list(request):
    posts = Post.objects.all().order_by('-created_at').prefetch_related('comments')
    context = {
        'posts': posts,
        'title': 'Posts List'
        }
    return render(request, 'posts_list.html', context)