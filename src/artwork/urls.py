from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^upload/$',views.upload_file,name='upload'),
    url(r'^art_info/$',views.art_info,name='art_info'),
    url(r'^(?P<artcontext>[a-z_]+)/(?P<art_id>[a-z0-9]+)$',views.art_view,name='art_view'),
    url(r'^(?P<artcontext>[a-z_]+)/$',views.art_view,name='art_view'),
    #------------------------ url(r'^personal/$',views.personal,name='personal')
]