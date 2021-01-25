from django.shortcuts import render
from .models import Post

# Create your views here.

def showblog(request):
	posts = Post.objects.all().order_by('-id')
	return render(request, 'blog/blog.html', {'posts': posts})