from django.db import models
from authentication.models import CustomUser


class VotingPoll(models.Model):
    text = models.CharField(max_length=256)
    published_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.text)


class VotingChoice(models.Model):
    question = models.ForeignKey(VotingPoll, on_delete=models.CASCADE, related_name="choices")
    text = models.CharField(max_length=1024)

    def __str__(self):
        return str(self.text)


class Vote(models.Model):
    choice = models.ForeignKey(VotingChoice, on_delete=models.CASCADE, related_name="votes")
    voter = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
