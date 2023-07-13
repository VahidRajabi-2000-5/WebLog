from django.shortcuts import render,get_object_or_404
from django.contrib.auth.models import User


from .models import Post

def post_list_view(request):
    posts = Post.objects.filter(status='Pub').order_by('-datetime_modified')
    return render(request,'blog/posts_list.html',{"posts":posts})
    
      
      
def post_detail_view(request,pk):
    post = get_object_or_404(Post,pk=pk)
    return render(request,'blog/post_detail.html',{"post":post})
    
# =======================
# def handling_404(request,exception):
#     return render (request,'blog/404.html') 
# =======================

def post_create_view(request):
    if request.method =="POST":
        print("POST Request")
        post_title = request.POST.get('title')
        post_text = request.POST.get('text')
        
        user = User.objects.all()[0]
        
        Post.objects.create(title=post_title,text=post_text,author=user,status='Pub')
    
    else:
        print("GET Request")
        
    return render(request,'blog/post_create.html',)














