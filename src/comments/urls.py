from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^like/$',views.like,name='like'),
    #------------------------ url(r'^personal/$',views.personal,name='personal')
]