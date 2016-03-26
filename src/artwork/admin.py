from django.contrib import admin
from .models import Artwork, ArtworkContext

# Register your models here.
admin.site.register(Artwork)
admin.site.register(ArtworkContext)