from django import forms

from comments.models import Comment

class CommentForm(forms.ModelForm):
    artwork = forms.IntegerField(widget=forms.HiddenInput())
    
    class Meta:
        model=Comment
        fields=('posted_by','comment',)