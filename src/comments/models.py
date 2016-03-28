from django.db import models
from artwork.models import Artwork

# Create your models here.
class Comment(models.Model):
    artwork = models.ForeignKey(Artwork)
    posted_by = models.CharField(max_length=60,blank=False)
    posted_at = models.DateTimeField(auto_now_add=True)
    comment = models.CharField(max_length=200)
    
    def __str__(self):
        return self.comment
    
    #Returns a "pretty" string of the date/time posted
    def time_posted(self):
        DATE_FORMAT = "%Y-%m-%d"
        TIME_FORMAT = "%I:%M"
        retval = self.posted_at.strftime("%s %s" % (DATE_FORMAT, TIME_FORMAT))
        return retval
    
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