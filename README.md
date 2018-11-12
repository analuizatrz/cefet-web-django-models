# cefet-web-django-models
Prática de Programação web

from music.models import *
from datetime import date
grunge = EstiloMusical.objects.create(nome="Grunge", surgimento=date(1980,1,1))
layne = Musico.objects.create(nome="Layne Staley", data_de_nascimento=date(1967,8,22), anos_de_carreira=23)
mike = Musico.objects.create(nome="Mike Starr", data_de_nascimento=date(1966,4,4),anos_de_carreira=30)


```sudo apt-get install python3-pip```

sudo apt-get install python3 pyhton3-pip

pip3 install django

python3 manage.py makemigrations

python3 manage.py migrate

python3 manage.py shell

