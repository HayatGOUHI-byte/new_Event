from django.conf.urls import url
from django.conf.urls import include


from . import views 

urlpatterns = [
    # url('', views.index),
    url('detail/<id_album>', views.detail),
    url('accueil/', views.accueil),

]