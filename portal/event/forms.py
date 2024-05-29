from django import forms
from event.models import Event

class EditForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ("name", "discription", "time", "date")


class AddForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ("name", "discription", "time", "date")