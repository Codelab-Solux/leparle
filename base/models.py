from django.db import models
from django.urls import reverse
from django.utils import timezone

# Create your models here.
class Sector(models.Model):
    name  = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(blank=True, null=True, upload_to = 'sectors')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('sector', kwargs={'pk': self.pk})
    
class Course(models.Model):
    sector = models.ForeignKey(
        Sector, on_delete=models.SET_NULL, blank=True, null=True,)
    title  = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255, blank=True, null=True)
    overview = models.TextField(blank=True, null=True)
    article = models.TextField(blank=True, null=True)
    video = models.FileField(blank=True, null=True, upload_to = 'videos')
    document = models.FileField(blank=True, null=True, upload_to = 'docs')
    is_popular = models.BooleanField(default=False)
    date_added = models.DateTimeField(blank=True, default=timezone.now)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('course', kwargs={'pk': self.pk})
    

class Blogpost(models.Model):
    sector = models.ForeignKey(
        Sector, on_delete=models.SET_NULL, blank=True, null=True,)
    title  = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255, blank=True, null=True)
    article = models.TextField(blank=True, null=True)
    image = models.ImageField(blank=True, null=True, upload_to = 'blogposts')
    date_added = models.DateTimeField( blank=True, default=timezone.now)


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blogpost', kwargs={'pk': self.pk})
