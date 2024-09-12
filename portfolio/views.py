from django.shortcuts import render

from portfolio.models import Project


# Create your views here.
def portofolio_view(request):
    return render(request, 'portfolio/index.html', {'projects': Project.objects.all()})
