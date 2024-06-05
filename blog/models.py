from django.db import models
from django.urls import reverse
from datetime import datetime, date

# Create your models here.
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('home')


class Post(models.Model):
    #header_image = models.ImageField(null=True, blank=True,upload_to="blogs/")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(max_length=255,blank=True, null=True)
    body_content = models.TextField(blank=True, null=True)
    post_date = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name='blog_post')
    likecount=models.IntegerField(blank=True, null=True,default=0)
    unlikecount=models.IntegerField(blank=True, null=True,default=0)
    commentcount=models.IntegerField(blank=True, null=True,default=0)
    answercount=models.IntegerField(blank=True, null=True,default=0)
    viewcount=models.IntegerField(blank=True, null=True,default=0)
    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.body_content

    def get_absolute_url(self):
        # return reverse('article_detail', args=(str(self.id)))
        return reverse('home')
class PostLike(models.Model):
    post=models.ForeignKey(Post, on_delete=models.CASCADE ,null=True, blank=True)
    user=models.ForeignKey(User, on_delete=models.CASCADE ,null=True, blank=True)
class PostDislike(models.Model):
    post=models.ForeignKey(Post, on_delete=models.CASCADE ,null=True, blank=True)
    user=models.ForeignKey(User, on_delete=models.CASCADE ,null=True, blank=True)

class AnswerQuestion(models.Model):
    body_content = models.TextField(blank=True, null=True)
    post=models.ForeignKey(Post, on_delete=models.CASCADE ,null=True, related_name='post', blank=True)
    user=models.ForeignKey(User, on_delete=models.CASCADE ,null=True, related_name='user', blank=True)
    answer_date = models.DateTimeField(auto_now_add=True)



class TotalData(models.Model):
    
    total_question = models.IntegerField(blank=True, null=True)
    total_answer = models.IntegerField(blank=True, null=True)
