# from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
	message = "Salut tout le monde"
	return HttpResponse(message)



def listing(request):
	artist = ARTISTS['francis-cabriel']['name']
	return HttpResponse(artist)