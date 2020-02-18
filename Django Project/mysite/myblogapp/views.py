from django.shortcuts import get_object_or_404,render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.http import HttpResponse
from myblogapp.models import BlogEntry,Comment
from django.template import loader
from django.views import generic
from django.contrib.auth.models import User
from myblogapp.forms import commentForm
# Create your views here.

def index(request):
    return HttpResponse("You are currently in myblogapp")

def landing(request):
    template = loader.get_template('myblogapp/landing.html')
    context = {
    }
    return HttpResponse(template.render(context, request))

def blogposts(request):
    template = loader.get_template('myblogapp/blogposts.html')
    latest_blog_posts = BlogEntry.objects.order_by('-blog_date_published')[:5]
    context = {
        'latest_blog_posts': latest_blog_posts,
    }
    return HttpResponse(template.render(context, request))

def blogpost(request,blog_id):
    blogpost = get_object_or_404(BlogEntry, pk=blog_id)
    comments = Comment.objects.select_related('blog').filter(blog=blog_id)
    context= {
        'blogpost': blogpost,
        'comments':comments
    }
    return render(request, 'myblogapp/blogpost.html', context)


def social(request):
    template = loader.get_template('myblogapp/social.html')
    context = {
    }
    return HttpResponse(template.render(context, request))

def aboutme(request):
    template = loader.get_template('myblogapp/aboutme.html')
    context = {
    }
    return HttpResponse(template.render(context, request))

def errorPage(request):
    template = loader.get_template('myblogapp/errorPage.html')
    context = {
    }
    return HttpResponse(template.render(context, request))

def blogpostcomment(request,blog_id):
     blogpost = get_object_or_404(BlogEntry, pk=blog_id)
     form = commentForm(request.POST)
     print(form)
     data=""
     if form.is_valid():
         data = form.cleaned_data.get("comment")
         print(data)

     user = get_object_or_404(User, pk=1)
     print(blogpost.blog_id)
     Comments = Comment()
     Comments.blog=blogpost
     Comments.comment_text = data
     Comments.comment_user = user
     if(data!=""):
        Comments.save()
     else:
         print("No Comment")
            
     # Always return an HttpResponseRedirect after successfully dealing
     # with POST data. This prevents data from being posted twice if a
     # user hits the Back button.
     return HttpResponseRedirect(reverse('myblogapp:blogpost', args=(blogpost.blog_id,)))
