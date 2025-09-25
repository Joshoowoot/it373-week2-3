from django.shortcuts import render

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