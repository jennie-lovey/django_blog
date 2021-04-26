from django.urls import path
from .views import BlogListView,BlogDetailView,BlogCreateView
from  . import views



urlpatterns=[
    path('blog_create/', BlogCreateView.as_view(), name='blog_create'),
    path('blog/<int:pk>/', BlogDetailView.as_view(), name='post_detail'),
    path('', BlogListView.as_view(), name='home'),

]