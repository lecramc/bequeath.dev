from django.urls import path

from blog import views

app_name = 'blog'

urlpatterns = [path('', views.blog_view, name='blog'), path('<int:pk>', views.post_view, name='post'),
 ]
