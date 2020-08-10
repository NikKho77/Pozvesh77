
from django.urls import path, include
from . import views
from .views import PostMainPageView,PhotoModelView,VideoModelView,ONasModelView

urlpatterns = [
  #  path('', views.home, name="home"),

    path('', PostMainPageView.as_view(), name = "home"),
    path('gallery.html/', PhotoModelView.as_view(), name = 'gallery'),
    path('video.html/', VideoModelView.as_view(), name = 'video'),
    path('video,html/', ONasModelView.as_view(), name= 'onas'),
]