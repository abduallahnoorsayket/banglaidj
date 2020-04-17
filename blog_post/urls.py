from django.conf.urls import url
from . import views
from django.urls import path

urlpatterns = [
    path('home/', views.home, name='home'),
    path('post-list/', views.post_list, name='post-list'),
    path('single-post/<post_id>/', views.single_post, name='single-post')
]