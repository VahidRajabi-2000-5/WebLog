from django.shortcuts import render,get_object_or_404

from .models import Post

def post_list_view(request):
    posts = Post.objects.filter(status='Pub').order_by('-datetime_modified')
    return render(request,'blog/posts_list.html',{"posts":posts})
    
      
      
def post_detail_view(request,pk):
    post = get_object_or_404(Post,pk=pk)
    return render(request,'blog/post_detail.html',{"post":post})
    
    
# def handling_404(request,exception):
#     return render (request,'blog/404.html')