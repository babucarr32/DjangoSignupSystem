from django.contrib import admin
from django.urls import path, include
from .views import signup
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('signup/', signup, name='signup'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
