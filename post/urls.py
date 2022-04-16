from django.urls import path

from .views import get_post_detail, index, get_post_list, PostCreateView

urlpatterns = [
    path('', index, name="index"),
    path('blog/posts/', get_post_list, name="post_list"),
    path('blog/post/<int:pk>/', get_post_detail, name="post_detail"),
    path('blog/category/<slug:slug>/', get_post_list, name="category_posts"),
    path('blog/post/create/', PostCreateView.as_view(), name="post_create")
]

# jailoo.kg/blog/post/1
# jailoo.kg/blog/post/2
# jailoo.kg/blog/post/5
