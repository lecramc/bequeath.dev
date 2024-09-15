from django.shortcuts import render

from blog.models import Post


# Create your views here.
def blog_view(request):
    """Blog view"""
    return render(request, "blog/index.html", posts=Post.objects.all())
