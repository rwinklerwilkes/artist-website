from django.shortcuts import render
from .models import Artwork, ArtworkContext
from comments.forms import CommentForm
from pip._vendor import requests
from .forms import ArtworkImageForm
from .utils import handle_uploaded_image

# Create your views here.
def art_view(request,artcontext):
    artwork_context = ArtworkContext.objects.get(created_for=artcontext)
    all_art = Artwork.objects.filter(created_for=artwork_context)
    comment_forms = {}
    if request.POST:
        for art in all_art:
            art_id = int(request.POST['artwork'])
            if art.id==art_id:
                comment_form = CommentForm(request.POST,initial={'artwork':art.id})
                if comment_form.is_valid():
                    comment = comment_form.save(commit=False)
                    comment.artwork = art
                    comment.save()
                else:
                    print(comment_form.errors)
            else:
                comment_form = CommentForm(initial={'artwork':art.id})
            comment_forms[art.id] = comment_form 
    else:
        for art in all_art:
            comment_forms[art.id] = CommentForm(initial={'artwork':art.id})
        
    return render(request,'artwork/'+artcontext+'.html',{'artwork':all_art,'comment_forms':comment_forms})

def upload_file(request):
    if request.method == 'POST':
        form = ArtworkImageForm(request.POST,request.FILES)
        if form.is_valid():
            artwork = form.save(commit=False)
            t = handle_uploaded_image(request.FILES['image'])
            #filename,image
            artwork.image.save(t[0],t[1])
            artwork.save()
    else:
        form = ArtworkImageForm()
    return render(request, 'artwork/upload.html', {'form': form})

#------------------------------------------------- def market_district(request):
    #--------- artwork_context = ArtworkContext.objects.get(created_for='ge_md')
    #------------- all_art = Artwork.objects.filter(created_for=artwork_context)
    #-- return render(request,'artwork/marketdistrict.html',{'artwork':all_art})
#------------------------------------------------------------------------------ 
#-------------------------------------------------------- def personal(request):
    #------ artwork_context = ArtworkContext.objects.get(created_for='personal')
