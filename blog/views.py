from django.shortcuts import render
from .models import Post


def home(request):
    info = {
        'post' : Post.objects.all()
    }
    return render(request, 'blog/Home.html',info)

def about(request):
    return render(request,'blog/About.html',{'title': 'About'})
