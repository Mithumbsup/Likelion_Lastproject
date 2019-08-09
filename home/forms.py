from django import forms
from .models import Post, Comment, Order

class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        fields={'title', 'brand', 'bad','component' ,'text','author', 'image',}

class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields={'text',}

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = {'product', 'orderer', 'postcode', 'address', 'phone1', 'phone2', 'email', 'message', 'price', 'delivery_price', 'total_price',}