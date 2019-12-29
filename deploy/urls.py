from django.contrib import admin
from django.urls import path, include
import accounts, home
from django.conf.urls.static import static
from django.conf import settings

from home import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('posts', views.PostViewSet)
router.register('comments', views.CommentViewSet)
router.register('orders', views.OrderViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', include('home.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('accounts.urls')),
    # drf로 api 만들어주기 
    path('api/', include(router.urls))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
