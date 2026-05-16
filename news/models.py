from django.db import models
from tinymce.models import HTMLField
from autoslug import AutoSlugField
class News(models.Model):
    news_title=models.CharField(max_length=100)
    news_des=HTMLField()
    form_pdf = models.FileField(upload_to='forms/', null=True, blank=True,max_length=500)

    news_slug=AutoSlugField(populate_from='news_title',unique=True,null=True,default=None)
    
# Create your models here.
