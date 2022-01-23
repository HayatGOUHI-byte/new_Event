# from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.


from .models import ALBUMS, ARTISTS


def accueil(request):
	return HttpResponse("Hello world")


# def detail(request, album_id):
	# id = int(album_id)
	# m = ARTISTS[id]
	# return HttpResponse("{}".format(m))


def search(request):
	obj = str(request.GET)
	query = request.GET['query']
	message = "proprietes GET : {} et requete : {}".format(obj, query)
	return HttpResponse(message)