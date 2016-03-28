from PIL import Image
from AbbyWebsite.settings import MEDIA_ROOT
from django.core.files import File
import hashlib
import io
import os

def handle_uploaded_image(i):
    image_str = b''
    for c in i.chunks():
        image_str += c
    
    max_width = 1920
    max_height = 1080
    imagefile  = io.BytesIO(image_str)
    img = Image.open(imagefile)
    if img.mode not in ('L', 'RGB'):
        img = img.convert('RGB')
    cur_width = img.size[0]
    cur_height = img.size[1]
    
    if cur_width > max_width:
        ratio = max_width/cur_width
        new_height = cur_height*ratio
        img = img.resize((max_width,new_height))
        cur_width = img.size[0]
        cur_height = img.size[0]
        
    if cur_height > max_height:
        ratio = max_height/cur_height
        new_width = cur_width*ratio
        img = img.resize((new_width,max_height))
        cur_width = img.size[0]
        cur_height = img.size[0]
    
    imagefile = io.BytesIO()
    filename = hashlib.md5(imagefile.getvalue()).hexdigest()+'.jpg'
    
    imagefile = open(os.path.join(MEDIA_ROOT,'artwork',filename),'w+')
    img.save(imagefile,'JPEG',quality=90)
    imagefile = open(os.path.join(MEDIA_ROOT,'artwork',filename), 'rb')
    content = File(imagefile)
    
    return (filename,content)
    