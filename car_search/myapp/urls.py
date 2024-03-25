from django.urls import path
from . import views
import csv
import random
import string

from .models import Unique_location, Car

urlpatterns = [
    path('', views.index, name='index'),
    path('create_cargo', views.create_cargo, name='create_cargo'),
    path('delete_cargo', views.delete_cargo, name='delete_cargo'),
    path('change_cargo', views.change_cargo, name='change_cargo'),
    path('change_car', views.change_car, name='change_car'),
    path('get_list_cargo', views.get_list_cargo, name='get_list_cargo'),
    path('information_about_cargo', views.information_about_cargo, name='information_about_cargo'),
]

def load_data_from_csv(file_path):
    with open(file_path, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            obj, created = Unique_location.objects.get_or_create(
                zip=int(row['zip']),
                defaults={
                    'lat' : float(row['lat']),
                    'lng' : float(row['lng']),
                    'city' : row['city'],
                    'state_name' : row['state_name']
                }
            )
            if not created:
                print(f'Object with zip={row["zip"]} updated')
    if len(Car.objects.all()) == 0:
        random_objects = Unique_location.objects.order_by('?')[:20]
        for item in random_objects:
            Car.objects.get_or_create(
                car_number= str(random.randint(1000, 9999))+random.choice(string.ascii_uppercase),
                defaults={
                    'location': item,
                    'lifting_capacity': random.randint(1, 1000)
                }
            )

