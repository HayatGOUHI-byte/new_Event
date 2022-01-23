from django.conf.urls import url
from django.conf.urls import include


from . import views 

urlpatterns = [
    url('detail/<int:id_album>/',views.detail),
    url('accueil/',views.accueil),
    url('album',views.album),

]