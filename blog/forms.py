from django import forms
from . import models

class SuggestionForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    sender = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)


class CommentForm(forms.ModelForm):
    class Meta:
        model = models.Comment
        fields=['name','text','created_date']
