from django.db import models
from django.conf import settings

# Create your models here.

class Etat(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True, default='')
    created_at = models.DateTimeField(blank=True, null=True,auto_now_add=True)
    updated_at = models.DateTimeField(blank=True, null=True,auto_now=True)
    
    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True, default='')
    created_at = models.DateTimeField(blank=True, null=True,auto_now_add=True)
    updated_at = models.DateTimeField(blank=True, null=True,auto_now=True)
    
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ['title']


class Article(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    category = models.ForeignKey(Category, related_name='listings', on_delete=models.SET_NULL, blank=True, null=True,)
    etat = models.ForeignKey(Etat, related_name='listings', on_delete=models.SET_NULL, blank=True, null=True,)
    quantity = models.IntegerField(blank=True, null=True, default=0)
    location = models.CharField(max_length=300, blank=True, null=True)
    is_enabled = models.BooleanField(default=True)
    # user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='listings', on_delete=models.SET_NULL, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True,auto_now_add=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('article:article_detail', kwargs={'pk': self.pk})

    class Meta:
        ordering = ['-created_at'] 
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'



class Image(models.Model):
    article = models.ForeignKey(Article, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='article_images/')
    created_at = models.DateTimeField(blank=True, null=True,auto_now_add=True)
    updated_at = models.DateTimeField(blank=True, null=True,auto_now=True)
    
    def __str__(self):
        return f"Image for {self.article.title}"
