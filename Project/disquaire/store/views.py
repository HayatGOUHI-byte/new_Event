# from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.


from .models import ARTISTS





def listing(request):
	return render(request,'listing.html')
		