from django import forms
from .models import Post, Comment, Order

class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        fields={'title', 'brand', 'component' ,'text','author', 'image',}

class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields={'text',}

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['name', 'amount', 'quantity']
        widgets = {
            'name': forms.TextInput(attrs={'readonly': 'readonly'}),
            'amount': forms.TextInput(attrs={'readonly': 'readonly'}),
            'quantity': forms.TextInput(attrs={'readonly': 'readonly'}),
        }