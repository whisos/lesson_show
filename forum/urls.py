from django.urls import path
from forum.views import *

urlpatterns = [
    path('', Forum_Themes_View.as_view(), name = "themes_list"),
    path('<int:pk>/', Posts_View.as_view(), name = "posts_list"),
    path('posts/<int:pk>/', Post_Detail_View.as_view(), name = "post_detail"),
    path('task_add/', PostAddView.as_view(), name="post_add"),
    path('<int:pk>/update/', PostUpdateView.as_view(), name = "post_update"),
    path('<int:pk>/delete/', PostDeleteView.as_view(), name = "post_delete"),
    path('comment_add/', CommentAddView.as_view(), name="comment_add"),
    path('comment/<int:comment_id>/like-toggle/', CommentLikeToggle.as_view(), name='comment-like-toggle'),
    path('theme_add/', ThemeAddView.as_view(), name = "theme_add"),
    path('theme/<int:pk>/update/', ThemeUpdateView.as_view(), name = "theme_update")
    

]

app_name = "forum"