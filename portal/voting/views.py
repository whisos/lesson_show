from django.shortcuts import render, redirect
from voting.models import VotingPoll, VotingChoice, Vote
from django.views.generic import ListView, DetailView, CreateView, DeleteView, View
from django.urls import reverse_lazy


def get_votes(request=None, user=None, poll=None, pk=None):
    if not user:
        if not request:
            raise Exception
        user = request.user
    if not poll:
        if not pk:
            raise Exception
        poll = VotingPoll.objects.get(pk=pk)
    votes = Vote.objects.filter(voter=user).filter(choice__question=poll)
    return votes


class PollListView(ListView):
    model = VotingPoll
    paginate_by = 10
    template_name = "voting/list.html"


class PollDetailView(DetailView):
    model = VotingPoll
    template_name = "voting/poll.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["voted"] = None
        try:
            vote = get_votes(
                request=self.request,
                pk=self.kwargs['pk']
            )[0]
            context["voted"] = vote.choice.pk
        finally:
            return context


class PollVote(View):
    def post(self, request, pk, *args, **kwargs):
        user = request.user
        if not user.is_authenticated:
            return redirect(reverse_lazy("login"))
        poll = VotingPoll.objects.get(pk=pk)
        self.remove_user_vote_if_exists(user, poll)
        new_choice_pk = request.POST.get('choice')
        self.user_vote(user, new_choice_pk)
        return redirect("voting_poll", pk=pk)

    def remove_user_vote_if_exists(self, user, poll):
        for vote in get_votes(user=user, poll=poll):
            vote.delete()

    def user_vote(self, user, new_choice_pk):
        new_choice = VotingChoice.objects.get(pk=new_choice_pk)
        Vote(
            choice=new_choice,
            voter=user
        ).save()


class PollCreateView(CreateView):
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


class PollDeleteView(DeleteView):
    model = VotingPoll
    template_name = "voting/poll_delete_confirmation.html"
    success_url = reverse_lazy("voting_list")
