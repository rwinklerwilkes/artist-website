from django.db import models
from artwork.models import Artwork

# Create your models here.
class Comment(models.Model):
    artwork = models.ForeignKey(Artwork)
    posted_by = models.CharField(max_length=60)
    comment = models.CharField(max_length=200)
    
class Like(models.Model):
    artwork = models.ForeignKey(Artwork)
    number = models.IntegerField(default=0)
    
    def get_likes(self):
        return self.number
    
    def add_like(self):
        self.number = self.number + 1
        return self.number
    
    def remove_like(self):
        if self.number > 0:
            self.number = self.number - 1
        return self.number