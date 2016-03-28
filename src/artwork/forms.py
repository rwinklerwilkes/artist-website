from django import forms

from artwork.models import Artwork

class ArtworkImageForm(forms.ModelForm):
    class Meta:
        model=Artwork
        fields=('created_for','name','description','created_on','image',)