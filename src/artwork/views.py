from django.shortcuts import render
from .models import Artwork, ArtworkContext

# Create your views here.
def art_view(request,artcontext):
    artwork_context = ArtworkContext.objects.get(created_for=artcontext)
    all_art = Artwork.objects.filter(created_for=artwork_context)
    return render(request,'artwork/'+artcontext+'.html',{'artwork':all_art})

#------------------------------------------------- def market_district(request):
    #--------- artwork_context = ArtworkContext.objects.get(created_for='ge_md')
    #------------- all_art = Artwork.objects.filter(created_for=artwork_context)
    #-- return render(request,'artwork/marketdistrict.html',{'artwork':all_art})
#------------------------------------------------------------------------------ 
#-------------------------------------------------------- def personal(request):
    #------ artwork_context = ArtworkContext.objects.get(created_for='personal')
