from django.conf.urls import url
from django.conf.urls import include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from . import views 


urlpatterns = [
    # url(r'^(?P<album_id>[0-9])/$',views.detail),  #regular expression
    url(r'index/',views.index, name="index"),
    url(r'listing/', views.listing, name="lists"),
    url(r'^detail/(?P<album_id>[0-9])/$', views.detail, name="details"),
    url(r'search/', views.search, name="search"), 
]



urlpatterns += staticfiles_urlpatterns()