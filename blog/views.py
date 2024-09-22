from django.shortcuts import render

from blog.models import Post


# Create your views here.
def blog_view(request):
    """Blog view"""
    posts = Post.objects.all()
    return render(request, "blog/index.html", {"posts": posts})

def post_view(request, pk):
    """Post view"""
    post = Post.objects.get(pk=pk)
    return render(request, "blog/post.html", {"post": post})
