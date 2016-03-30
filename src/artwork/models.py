from django.db import models
from sorl.thumbnail import ImageField
from PIL import Image
from io import BytesIO

class ArtworkContext(models.Model):
    created_for = models.SlugField(unique=True,primary_key=True)
    description=models.CharField(max_length=100)
    
    def __str__(self):
        return self.description

class Artwork(models.Model):
    created_for=models.ForeignKey(ArtworkContext)
    name=models.CharField(max_length=100)
    description=models.CharField(max_length=200)
    created_on = models.DateField(blank=True,null=True)
    medium = models.CharField(max_length=100,blank=True,null=True)
    width = models.IntegerField(blank=True,null=True)
    height = models.IntegerField(blank=True,null=True)
    image = ImageField(upload_to='artwork/',blank=True,null=True)
    
    def get_image(self):
        if self.image is not None:
            return self.image.url
        else:
            return '#'
        
    def __str__(self):
        return self.name
        