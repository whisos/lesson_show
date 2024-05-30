from django.shortcuts import render, redirect
from voting.models import VotingPoll, VotingChoice, Vote
from django.views.generic import ListView, DetailView, CreateView, DeleteView
from django.urls import reverse_lazy


class VotingPollListView(ListView):
    model = VotingPoll
    paginate_by = 10
    template_name = "voting/list.html"


class VotingPollDetailView(DetailView):
    model = VotingPoll
    template_name = "voting/poll.html"


class VotingPollCreateView(CreateView):
    model = VotingPoll

    def get(self, request, *args, **kwargs):
        return render(request, "voting/create_poll.html")

    def post(self, request, *args, **kwargs):
        question_name = request.POST.get('poll-text')
        voting_poll = VotingPoll(text=question_name)
        voting_poll.save()

        choices = [
            request.POST.get('choice-text-1'),
            request.POST.get('choice-text-2'),
            request.POST.get('choice-text-3'),
            request.POST.get('choice-text-4'),
            request.POST.get('choice-text-5'),
        ]

        for choice_text in choices:
            if not choice_text:
                continue

            choice = VotingChoice(
                text=choice_text,
                question=voting_poll
            )
            choice.save()
        return redirect("voting_poll", pk=voting_poll.pk)


class VotingPollDeleteView(DeleteView):
    model = VotingPoll
    template_name = "voting/poll_delete_confirmation.html"
    success_url = reverse_lazy("voting_list")