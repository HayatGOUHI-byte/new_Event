# from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, loader
# Create your views here.

from .models import Album, Artist, Contact, Booking





def accueil(request):
	return HttpResponse("Hello world")


# def detail(request, album_id):
	# id = int(album_id)
	# m = ARTISTS[id]
	# return HttpResponse("{}".format(m))



def index(request):
	albums = Album.objects.filter(availible=True).order_by('-created_at')[:12]
	formatted_album = ["<li>{}</li>".format(album.title) for album in albums ]
	template = loader.get_template("store/index.html")
	context = {
	'albums': albums
	}
	return HttpResponse(template.render(context, request=request))
	



def listing(request):
	albums = Album.objects.filter(availible=True)
	formatted_albums = ["<li>{}</li>".format(album.title) for album in albums]
	message = """<ul>{}</ul>""".format("\n".join(formatted_albums))
	return HttpResponse(render(request, 'store/listing.html'))

def detail(request, album_id):
	album = Album.objects.get(pk = album_id)
	artists = " ".join([artist.name for artist in album.artists.all()])
	message = "le nom de l'album est {}.Il a ete ecrit par {}".format(album.title, artists)
	query = request.GET['query']
	message = "proprietes GET : {} et requete : {}".format(obj, query)
	return HttpResponse(render(request, 'store/detail.html'))


def search(request):
	query = request.GET.get('query')
	if not query:
		albums = Album.objects.all()
	else:
		albums = Album.objects.filter(title__icontains=query)

		if not albums.exists():
			albums = Album.objects.filter(artist__name__icontains=query)

		if not albums.exists():
			message = "Misère de Misère on n 'a rien trouve"
		else:
			albums = ["<li>{}</li>".format(album.title) for album in albums]
			message = """
			Nous avons rien trouvé """.format("</li><li>".join(albums))

		return HttpResponse(message)