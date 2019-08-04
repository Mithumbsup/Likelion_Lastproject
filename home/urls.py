from django.urls import path
from . import views

urlpatterns = [
    path('home/',views.home, name='home'),
    path('post/<int:post_id>/', views.mypage, name='mypage'),
    path('post/order/', views.post_order,name='order'),
    path('post/order_list/', views.order_list,name='order_list'),
    path('post/<int:post_id>/edit/',views.post_edit,name='edit'),
    path('post/<int:post_id>/delete',views.post_delete, name='delete'),
    path('post/<int:post_id>/comment/',views.add_comment,name='add_comment'),
    path('comment/<int:comment_id>/delete/',views.comment_delete,name='comment_delete'),
]
