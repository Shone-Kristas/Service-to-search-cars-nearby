from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods
from geopy.distance import distance

from .models import Car, Cargo, Unique_location
def index(request):
    return render(request, 'myapp/index.html', {'title': 'Главная страница'})


@require_http_methods(['POST'])
def create_cargo(request):
    pick_up_add = request.POST['pick_up_add']
    delivery_add = request.POST['delivery_add']
    weight_add = request.POST['weight_add']
    description_add = request.POST['description_add']
    if not (pick_up_add and Unique_location.objects.filter(zip=pick_up_add).exists()):
        return HttpResponseNotFound("<h2>Pick-up ZIP does not exist</h2>")

    if not (delivery_add and Unique_location.objects.filter(zip=delivery_add).exists()):
        return HttpResponseNotFound("<h2>Delivery ZIP does not exist</h2>")

    if not weight_add or not weight_add.isdigit() or not (1 <= int(weight_add) <= 1000):
        return HttpResponseNotFound("<h2>Weight must be a number between 1 and 1000</h2>")

    if not description_add:
        return HttpResponseNotFound("<h2>Description is required</h2>")

    Cargo.objects.create(
        pick_up=Unique_location.objects.get(zip=pick_up_add),
        delivery=Unique_location.objects.get(zip=delivery_add),
        weight=weight_add,
        description=description_add
    )

    return HttpResponseRedirect("/")

@require_http_methods(['POST'])
def delete_cargo(request):
    id_del = request.POST['id_del']
    if id_del is not None and id_del.isdigit():
        if Cargo.objects.filter(id=id_del).exists():
            Cargo.objects.get(id=id_del).delete()
            return redirect('index')
        else:
            return HttpResponseNotFound("<h2>Could not find cargo with ID: {}</h2>".format(id_del))
    else:
        return HttpResponseNotFound("<h2>ID must be a number</h2>")

@require_http_methods(['POST'])
def change_cargo(request):
    id_cargo = request.POST['id_cargo']
    weight_editing = request.POST['weight_editing']
    description_editing = request.POST['description_editing']
    if id_cargo is None or not id_cargo.isdigit() or not Cargo.objects.filter(id=id_cargo).exists():
        return HttpResponseNotFound("<h2>Something wrong with ID: {}</h2>".format(id_cargo))
    if weight_editing != '' and (not weight_editing.isdigit() or not (1 <= int(weight_editing) <= 1000)):
        return HttpResponseNotFound("<h2>Weight must be a number between 1 and 1000</h2>")
    obj = Cargo.objects.get(id=id_cargo)
    if weight_editing != '':
        obj.weight = weight_editing
    if description_editing != '':
        obj.description = description_editing
    obj.save()
    return redirect('index')

@require_http_methods(['POST'])
def change_car(request):
    id_car = request.POST['id_car']
    location_editing = request.POST['location_editing']
    if id_car is None or not id_car.isdigit() or not Car.objects.filter(id=id_car).exists():
        return HttpResponseNotFound("<h2>Something wrong with ID: {}</h2>".format(id_car))
    if not (location_editing and Unique_location.objects.filter(zip=location_editing).first()):
        return HttpResponseNotFound("<h2>Pick-up ZIP does not exist</h2>")
    unique_location_editing = Unique_location.objects.filter(zip=location_editing).first()
    obj = Car.objects.get(id=id_car)
    obj.location = unique_location_editing
    obj.save()
    return redirect('index')
@require_http_methods(['POST'])
def get_list_cargo(request):
    list = []
    data_cargo = Cargo.objects.all()
    data_cars = Car.objects.all()
    for item in data_cargo:
        total = 0
        some = {}
        city_pick_up = item.pick_up.city
        some['city_pick_up'] = city_pick_up
        path_pick_up = (item.pick_up.lat, item.pick_up.lng)
        city_delivery = item.delivery.city
        some['city_delivery'] = city_delivery
        for location_cars in data_cars:
            path_car = (location_cars.location.lat, location_cars.location.lng)
            summ_path = distance(path_pick_up, path_car).miles
            if summ_path <= 450:
                total += 1
        some['total'] = total
        list.append(some)
    return render(request, 'myapp/index.html', {'list': list})
@require_http_methods(['POST'])
def information_about_cargo(request):
    slovar = {}
    id_cargo = request.POST['id_cargo']
    if id_cargo is None or not id_cargo.isdigit() or not Cargo.objects.filter(id=id_cargo).exists():
        return HttpResponseNotFound("<h2>Something wrong with ID: {}</h2>".format(id_cargo))
    data_cargo = Cargo.objects.get(id=id_cargo)
    data_cars = Car.objects.all()
    slovar['location_pick_up'] = data_cargo.pick_up.city
    slovar['location_delivery'] = data_cargo.delivery.city
    slovar['weight_cargo'] = data_cargo.weight
    slovar['description_cargo'] = data_cargo.description
    path_pick_up = (data_cargo.pick_up.lat, data_cargo.pick_up.lng)
    list = []
    for item in data_cars:
        slovar2 = {}
        path_car = (item.location.lat, item.location.lng)
        slovar2['number'] = item.car_number
        slovar2['path'] = distance(path_pick_up, path_car).miles
        list.append(slovar2)
    slovar['ghf'] = list

    return render(request, 'myapp/index.html', {'slovar': slovar})