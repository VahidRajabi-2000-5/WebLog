from django.shortcuts import render,get_object_or_404,redirect,reverse


from .models import Post
from .forms import NewPostForm

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
    if request.method =='POST':
        form = NewPostForm(request.POST)
        if form.is_valid():
            # instance=form.save()
            post = form.save()
            # post_id = form.instance.pk
            form =NewPostForm()
            return redirect(post.get_absolute_url())
    else:
        form = NewPostForm()
        
    return render(request,'blog/post_create.html',{'form':form})


def post_update_view(request,pk):
    post=get_object_or_404(Post,pk=pk)
    form = NewPostForm(request.POST or None,instance=post)
    if form.is_valid():
        form.save()
        return redirect(post.get_absolute_url())

    return render(request,'blog/post_create.html',{'form':form})



def post_delete_view(request,pk):
    post = get_object_or_404(Post,pk=pk)
    if request.method =="POST":
        post.delete() 
        return redirect('posts_list')
    
    return render(request,'blog/post_delete.html',{'post':post})
        

