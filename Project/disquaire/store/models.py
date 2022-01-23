from django.db import models

# Create your models here.


ARTISTS = {
'francis-cabriel' : {'name': 'Francis Cabriel'},
'lej': {'name': 'Elijay'},
'rosana': {'name': 'Rosana'},
'maria': {'name': 'Maria Dolores Pradera'},
}


ALBUMS = [
{'name': 'Sarbacane', 'artists': [ARTISTS['francis-cabrel']]},
{'name': 'la dalle', 'artists': [ARTISTS['lej']]},
{'name': 'Luna Nueva', 'artists': [ARTISTS['rosana'], ARTISTS['maria']]}
]