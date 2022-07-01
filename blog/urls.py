from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostList.as_view(), name='blog-home'),
    path('article/<int:pk>', views.PostDetail.as_view(), name='article-detail'),
    path('about/', views.about, name='blog-about'),
    path('news/', views.news, name='blog-news'),
    path('add-post/', views.AddPostView.as_view(),name='add-post'),
    path('article/edit/<int:pk>', views.UpdatePostView.as_view(), name='update-post'),
    #path('<int:id>/delete-post',views.delete_post,name='delete_post'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('add-category', views.AddCategoryView.as_view(), name='add-category'),
    path('category/<str:cats>/', views.CategoryView, name='category'),
    path('category-list/', views.CategoryListView, name='category-list'),
    path('like/<int:pk>', views.LikeView, name='like_post')
    ]