from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
    # root goes to the index
    url(r'^$', views.index),
]