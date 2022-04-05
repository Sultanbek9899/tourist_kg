from django.urls import path

from .views import get_post_detail, index, get_post_list

urlpatterns = [
    path('', index, name="index"),
    path('blog/posts/', get_post_list, name="post_list"),
    path('blog/post/<int:pk>/', get_post_detail, name="post_detail"),
]

# jailoo.kg/blog/post/1
# jailoo.kg/blog/post/2
# jailoo.kg/blog/post/5
