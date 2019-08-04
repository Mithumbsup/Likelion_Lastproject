from django.db import models
from django.utils import timezone
from django.conf import settings
# Create your models here.

class Post(models.Model):
    author=models.ForeignKey('auth.User',on_delete=models.CASCADE)
    title=models.CharField(max_length=200)
    text=models.TextField()

    def published(self):
        self.save()

    def __str__(self):
        return self.title
    
    def summary(self):
        a =[]
        a.append(self.title)

        if len(a[-1])>6:
            return self.title[:6]+'...'
        else:
            return self.title

class Comment(models.Model):
    post=models.ForeignKey('home.Post',related_name='comments', on_delete=models.CASCADE)
    nickname=models.CharField(max_length=200)
    text=models.TextField()
    created_date=models.DateTimeField(default=timezone.now)
   
    def __str__(self):
        return self.text

class Order(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE, )
    name = models.CharField(max_length=100, verbose_name='상품명')
    amount = models.PositiveIntegerField(verbose_name='결제금액')
    quantity = models.IntegerField(default=1)
    # products = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='order_product')
    order_date = models.DateTimeField(auto_now_add=True)

    #모델 인스턴스를 아이디 값 내림차순 정렬
    class Meta:
        ordering = ('-id',)

    def __str__(self):
        return '{} by {}'.format(self.products.name, self.user)
