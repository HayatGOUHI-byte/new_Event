from django.conf.urls import url
from django.conf.urls import include


from . import views 


urlpatterns = [
    # url(r'^(?P<album_id>[0-9])/$',views.detail),  #regular expression
    url('index/',views.index),
    url('listing/', views.listing),
    url('detail/(?P<album_id>[0-9])/$', views.detail),
    url('search/', views.search),
  
]