from django.urls import path

from . import views
app_name = 'myblogapp'
urlpatterns = [
    path('', views.index, name='index'),
    path('landing/', views.landing, name='landing'),
    path('social/', views.social, name='social'),
    path('aboutme/', views.aboutme, name='aboutme'),
    path('errorPage/', views.errorPage, name='errorPage'),
    path('blogposts/', views.blogposts, name='blogposts'),
    path('blogposts/<int:blog_id>/', views.blogpost, name='blogpost'),
    path('blogposts/blogpost/blogpostcomment/<int:blog_id>/', views.blogpostcomment, name='blogpost_comment')

    
]