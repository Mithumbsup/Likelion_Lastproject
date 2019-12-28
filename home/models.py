from django.db import models
from django.utils import timezone
from django.conf import settings
# Create your models here.

class Post(models.Model):
    author=models.ForeignKey('auth.User',on_delete=models.CASCADE)
    brand=models.CharField(max_length=200)
    title=models.CharField(max_length=200)
    text=models.TextField()
    component=models.TextField()
    image = models.ImageField(upload_to="images/")
    bad = models.TextField()
    
    def published(self):
        self.save()

    def __str__(self):
        return self.title

    def component_as_list(self):
        return self.component.split('\n')

class Comment(models.Model):
    post=models.ForeignKey('home.Post',related_name='comments', on_delete=models.CASCADE)
    nickname=models.CharField(max_length=200)
    text=models.TextField()
    created_date=models.DateTimeField(default=timezone.now)
   
    def __str__(self):
        return self.text

class Order(models.Model):
    writer = models.CharField(max_length=200, null=True)
    product = models.CharField(max_length=200, blank=False)
    orderer = models.CharField(max_length=200, blank=False)
    postcode = models.CharField(max_length=100, blank=False)
    address = models.CharField(max_length=800, blank=False)
    phone1 = models.CharField(max_length=100, blank=False)
    phone2 = models.CharField(max_length=100, null=True)
    email = models.EmailField(max_length=200, null=True)
    message = models.TextField(blank=True)
    created_date = models.DateTimeField(blank=True, default=timezone.now)
    price = models.IntegerField(blank=True)
    delivery_price = models.IntegerField(blank=True, null=True)
    total_price = models.IntegerField(blank=True)

   
    def __str__(self):
        return self.order