from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('posts', views.PostViewSet)
router.register('comments', views.CommentViewSet)
router.register('orders', views.OrderViewSet)

urlpatterns = [
    path('home/',views.home, name='home'),
    path('mypage/', views.mypage, name='mypage'),
    path('post/<int:post_id>',views.detail, name = 'detail'),
    path('post/order/', views.post_order,name='order'),
    path('order/complete', views.order_save, name='order_save'),
    path('post/order_list/', views.order_list,name='order_list'),
    path('post/new/', views.post_new, name = 'new'),
    path('post/<int:post_id>/edit/',views.post_edit,name='edit'),
    path('post/<int:post_id>/delete',views.post_delete, name='delete'),
    path('post/<int:post_id>/comment/',views.add_comment,name='add_comment'),
    path('comment/<int:comment_id>/delete/',views.comment_delete,name='comment_delete'),
    
    # 
    path('api/', include(router.urls))
]
