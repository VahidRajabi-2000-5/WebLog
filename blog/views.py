from django.shortcuts import render

from .models import Post

def post_list_view(request):
    posts = Post.objects.all().filter(status='Pub')
    return render(request,'blog/posts_list.html',{"posts":posts})
    
     