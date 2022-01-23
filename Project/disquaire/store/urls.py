from django.conf.urls import url
from django.conf.urls import include


from . import views 


urlpatterns = [
    # url(r'^(?P<album_id>[0-9])/$',views.detail),  #regular expression
    url('accueil/',views.accueil),
    url(r'^search/$', views.search),
]