from django import forms
from forum.models import Task, Comment

class TaskAdd(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["name", "description", "status", "priority", "start_date", "dead_line", "creator"]

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["content", "media"]
        widgets = {
            "media": forms.FileInput()

        }


class TaskFilterForm(forms.Form):
    STATUS_CHOICES = [
        ("", "Всі"),
        ("notdone", "Not Done"),
        ("in_progress", "In Progress"),
        ("done", "Done")
    ]

    status = forms.ChoiceField(choices=STATUS_CHOICES, required=False, label="Статус")