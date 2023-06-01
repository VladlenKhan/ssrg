from django.urls import path
from .views import *


urlpatterns = [
    path('',home,name='home'),
    path('login/',login_view,name='login'),
    path('logout/', user_logout, name='logout'),
    path('register/',register,name='register'),
    path('about_article1/',about_article1, name='about_article1'),
    path('about_article2/',about_article2, name='about_article2'),
    path('about_article3/',about_article3, name='about_article3'),
    path('about_article4/',about_article4, name='about_article4'),
    path('about_article5/',about_article5, name='about_article5'),
    path('about_article6/',about_article6, name='about_article6'),
    path('about_article7/',about_article7, name='about_article7'),
    path('about_article8/',about_article8, name='about_article8'),
    path('about_article9/',about_article9, name='about_article9'),
    
    # user
    path('user/<str:username>/', user_view, name='user'),
    path('user/<str:username>/<slug:category_slug>', user_view, name='user_blogs'),
    path('user/<str:username>/edit_user/',edit_user,name='edit_user'),
    path('user/<str:username>/edit_user/change_password/',change_password,name='change_password'),
    path('add_post/',add_post,name='add_post'),
    
    # blogs
    path('blogs/', blogs_view, name='blogs'),
    path('blog/<int:pk>/edit/', edit_blog, name='edit_blog'),
    path('delete_record/<int:pk>', delete_record, name='delete_record'),
    path('blog_detail/<int:pk>/', blog_detail, name='blog_detail'),
    path('blogs/<slug:category_slug>/', blogs_view, name='blogs_by_category'),

    # search
    path('search_result/', search_result, name='search_result'),

    # dowload file
    path('download_file/<int:pk>/', download_file, name='download_file'),
]