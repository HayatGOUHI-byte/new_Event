# from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.


from .models import ARTISTS


def accueil(request):
	return HttpResponse("Hello world")

def detail(request, id_album):
	id = int(id_album)
	album = ALBUMS[id]
	return HttpResponse(album)
		