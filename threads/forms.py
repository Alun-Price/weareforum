from django import forms
from .models import Thread, Posts, Poll, PollSubject


class ThreadForm(forms.ModelForm):
    name = forms.CharField(label="Thread name")
    is_a_poll = forms.BooleanField(label="Include a poll?", required=False)

    class Meta:
        model = Thread
        fields = {'name'}


class PostForm(forms.ModelForm):
    class Meta:
        model = Posts
        fields = ['comment']


# Poll and PollSubject Forms

class PollForm(forms.ModelForm):
    question = forms.CharField(label="What is you poll about?")

    class Meta:
        model = Poll
        fields = ['question']


class PollSubjectForm(forms.ModelForm):
    name = forms.CharField(label="Poll subject name", required=True)

    def __init__(self, *args, **kwargs):
        super(PollSubjectForm, self).__init__(*args, **kwargs)

        self.empty_permitted = False

    class Meta:
        model = PollSubject
        fields = ['name']
