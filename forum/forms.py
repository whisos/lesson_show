from django import forms
from forum.models import Forum_post, Comment

class PostAdd(forms.ModelForm):
    class Meta:
        model = Forum_post
        fields = ["title", "content", "author", "theme", "created_at"]

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["content", "media"]
        widgets = {
            "media": forms.FileInput()

        }
