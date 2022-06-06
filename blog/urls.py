from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostList.as_view(), name='blog-home'),
    path('about/', views.about, name='blog-about'),
    path('news/', views.news, name='blog-news'),
]
