from django.urls import path
from .views import BlogListWiev, BlogDetailView,BlogCreateView,BlogUpdateView,BlogDeleteView#import view

# www.site.com
urlpatterns = [
    path('', BlogListWiev.as_view(), name='home'),
    path('post/<int:pk>/',BlogDetailView.as_view(),name='post_detail'),
    path('post/new/',BlogCreateView.as_view(),name='post_new'),
    path('post/<int:pk>/edit/',BlogUpdateView.as_view(),name='post_edit'),
    path('post/<int:pk>/delete/',BlogDeleteView.as_view(),name='post_delete'),
]
