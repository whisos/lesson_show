from django.shortcuts import render
from voting.models import VotingPoll, VotingChoice, Vote
from django.views.generic import ListView, DetailView


class VotingPollListView(ListView):
    model = VotingPoll
    paginate_by = 10
    template_name = "voting/list.html"


class VotingPollDetailView(DetailView):
    model = VotingPoll
    template_name = "voting/poll.html"
