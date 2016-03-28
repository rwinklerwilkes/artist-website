from django.http import JsonResponse
from artwork.models import Artwork
from comments.models import Like,Comment
from django.shortcuts import get_object_or_404

# Create your views here.
def like(request):
    if request.POST:
        artwork_id = request.POST['artwork_id']
        cur_artwork = Artwork.objects.get(id=artwork_id)
        #get_or_create returns a tuple, I don't care if it was created or not
        #so, only look at the 0th element of the tuple
        cur_like = Like.objects.get_or_create(artwork=cur_artwork)[0]
        number_of_likes = cur_like.add_like()
        cur_like.save()
    else:
        number_of_likes = 0
    out_dict = {'likes':number_of_likes}
    return JsonResponse(out_dict)

def get_comments(request):
    out_dict = {'comments':[]}
    if request.GET:
        art_id = request.GET['artwork_id']
        artwork = get_object_or_404(Artwork,id=art_id)
        all_comments = Comment.objects.filter(artwork=artwork).order_by('-posted_at')
        for comment in all_comments:
            cur_comment_list = [comment.time_posted(),comment.posted_by,comment.comment]
            out_dict['comments'].append(cur_comment_list)
    return JsonResponse(out_dict)