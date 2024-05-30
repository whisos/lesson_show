from django.urls import path
from voting.views import VotingPollListView, VotingPollDetailView, VotingPollCreateView

urlpatterns = [
    path('', VotingPollListView.as_view(), name="voting_list"),
    path('<int:pk>/', VotingPollDetailView.as_view(), name="voting_poll"),
    path('create/', VotingPollCreateView.as_view(), name="create_poll"),
]
