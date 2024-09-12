from django.shortcuts import render


# Create your views here.
def blog_view(request):
    """Blog view"""
    return render(request, "blog/index.html")
