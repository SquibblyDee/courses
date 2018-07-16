from django.conf.urls import url
from . import views

urlpatterns = [
    # root goes to the index
    url(r'^$', views.index),
    # this goes to the page to select course to destroy
    url(r'courses/destroy/(?P<id>\d+)', views.destroy),
    # this actually destroys the selected course
    url(r'courses/process/destroy/(?P<id>\d+)', views.processdestroy),
    # this proccesses new courses when they are added
    url(r'process', views.process),
]