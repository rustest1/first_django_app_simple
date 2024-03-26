from django.shortcuts import render
from .models import Post

def index(request):
    posts = Post.objects.all().order_by('-date_posted')
    return render(request, 'simp_blog1/index.html', {'posts': posts})
