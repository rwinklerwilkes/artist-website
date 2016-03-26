from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^(?P<artcontext>[a-z_]+)/$',views.art_view,name='art_view'),
    #------------------------ url(r'^personal/$',views.personal,name='personal')
]