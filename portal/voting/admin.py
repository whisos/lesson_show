from django.contrib import admin
from voting.models import VotingPoll, VotingChoice, Vote

admin.site.register(VotingPoll)
admin.site.register(VotingChoice)
admin.site.register(Vote)
