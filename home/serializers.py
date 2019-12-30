from home.models import Post, Order, Comment
from rest_framework import serializers


class PostSerializer(serializers.HyperlinkedModelSerializer) :
    class Meta:
        model = Post
        fields = ('brand','title','text','component','image','bad' )
#'author',

class CommentSerializer(serializers.HyperlinkedModelSerializer) :
    class Meta:
        model = Comment
        fields = '__all__'

class OrderSerializer(serializers.HyperlinkedModelSerializer) :
    class Meta:
        model = Order
        fields = '__all__'