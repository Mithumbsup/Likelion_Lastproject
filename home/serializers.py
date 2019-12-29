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
        fields = ('post','nickname','text','created_date' )

class OrderSerializer(serializers.HyperlinkedModelSerializer) :
    class Meta:
        model = Order
        fields = ('writer','product','orderer','postcode','address','phone1','phone2',
                  'email', 'message', 'created_date', 'price', 'delivery_price','total_price'
                 )