from django.db import models
from authentication.models import *
# Create your models here.
from django.utils.text import slugify

from django.conf import settings

class Roadmap(models.Model):
    roadmap_name = models.CharField(max_length=100)
    roadmap_slug = models.SlugField(unique=True,blank=True)  # Add a SlugField for the slug
    roadmap_image = models.ImageField(upload_to='roadmap_images/',blank=True)  # Add an ImageField for the image

    my_order = models.PositiveSmallIntegerField("Position", null=True)

    def __str__(self):
        return self.roadmap_name


    class Meta:
        ordering = ['my_order']
        
    def save(self, *args, **kwargs):
            if not self.roadmap_slug:
                # Generate the slug from the roadmap_name
                self.roadmap_slug = slugify(self.roadmap_name)
            super().save(*args, **kwargs)

class Topic(models.Model):
    topic_name = models.CharField(max_length=100)
    roadmap = models.ForeignKey(Roadmap, on_delete=models.CASCADE)

    def __str__(self):
        return self.topic_name

class Subtopic(models.Model):
    subtopic_name = models.CharField(max_length=100)
    subtopic_link = models.URLField()
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    roadmap = models.ForeignKey(Roadmap, on_delete=models.CASCADE)
    my_order = models.PositiveSmallIntegerField("Position", null=True)

    def __str__(self):
        return self.subtopic_name
    
    class Meta:
        ordering = ['my_order']
        


class TopicStatus(models.Model):
    subtopic_status = models.ForeignKey(Subtopic, on_delete=models.CASCADE ,default="Not Started")
    user_link = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE, )
    def __str__(self):
        return self.subtopic_status