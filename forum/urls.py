from django.urls import path
from forum.views import *

urlpatterns = [
    path('', Forum_Themes_View.as_view(), name = "themes_list"),
    path('<int:pk>/', Post_Detail_View.as_view(), name = "post_detail"),
    path('task_add/', PostAddView.as_view(), name="post_add"),
    path('<int:pk>/update/', PostAddView.as_view(), name = "post_update"),
    path('<int:pk>/delete/', PostDeleteView.as_view(), name = "post_delete"),
    path('comment_add/', CommentAddView.as_view(), name="comment_add"),
    path('comment/<int:comment_id>/like-toggle/', CommentLikeToggle.as_view(), name='comment-like-toggle')
    

]

app_name = "forum"