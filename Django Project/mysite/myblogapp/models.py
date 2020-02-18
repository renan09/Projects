

# Create your models here.
from django.db import models
from django.utils import timezone
import datetime
from django.contrib.auth.models import User

STATUS = (
    (0,"Draft"),
    (1,"Publish")
)
class BlogEntry(models.Model):
    blog_id=models.AutoField(primary_key=True)
    blog_author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_posts')
    blog_Name = models.TextField(max_length=200)
    blog_Description = models.TextField(max_length=2000)
    blog_status=models.IntegerField(choices=STATUS, default=0)
    blog_date_created = models.DateTimeField('Blog Date Created',auto_now_add=True)
    blog_date_published = models.DateTimeField('Blog Date Published',auto_now=True)
    def __str__(self):
        return self.blog_Description
    def was_published_recently(self):
        return self.blog_date_published >= timezone.now() - datetime.timedelta(days=1)
    class Meta:
        ordering = ['-blog_date_created']

class Comment(models.Model):
    blog = models.ForeignKey(BlogEntry, on_delete=models.CASCADE)
    comment_text = models.CharField(max_length=200)
    comment_user = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_comment')
    def __str__(self):
        return self.comment_text        


