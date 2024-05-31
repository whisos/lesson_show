from django import forms
from forum.models import Forum_post, Comment, Forum_Theme

class PostAdd(forms.ModelForm):
    class Meta:
        model = Forum_post
        fields = ["title", "content", "theme"]

        widgets = {
            'theme': forms.HiddenInput()
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["content"]

class ThemeAdd(forms.ModelForm):
    class Meta:
        model = Forum_Theme
        fields = ["name", "description"]