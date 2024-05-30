from django.urls import path
import voting.views as voting

urlpatterns = [
    path('', voting.PollListView.as_view(), name="voting_list"),
    path('<int:pk>/', voting.PollDetailView.as_view(), name="voting_poll"),
    path('<int:pk>/delete', voting.PollDeleteView.as_view(), name="delete_poll"),
    path('<int:pk>/vote', voting.PollVote.as_view(), name="vote_poll"),
    path('create/', voting.PollCreateView.as_view(), name="create_poll"),
]
