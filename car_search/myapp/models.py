from django.core.validators import MaxValueValidator, RegexValidator
from django.db import models

class Unique_location(models.Model):
    zip = models.CharField(validators=[RegexValidator(regex='^[0-9]*$', message='Пожалуйста, введите только цифры')])
    lat = models.FloatField()
    lng = models.FloatField()
    city = models.CharField(max_length=100)
    state_name = models.CharField(max_length=150)

class Cargo(models.Model):
    pick_up = models.ForeignKey(Unique_location, on_delete=models.CASCADE, related_name='pick_up_location', validators=[RegexValidator(regex='^[0-9]*$')])
    delivery = models.ForeignKey(Unique_location, on_delete=models.CASCADE, related_name='delivery_location', validators=[RegexValidator(regex='^[0-9]*$')])
    weight = models.IntegerField(default=1, validators=[MaxValueValidator(1000), RegexValidator(regex='^[0-9]*$')])
    description = models.CharField()

class Car(models.Model):
    car_number = models.CharField(max_length=5, validators=[RegexValidator(regex='^[0-9]{4}[A-Z]$')])
    location = models.ForeignKey(Unique_location, on_delete=models.CASCADE, validators=[RegexValidator(regex='^[0-9]*$')])
    lifting_capacity = models.IntegerField(default=1, validators=[MaxValueValidator(1000), RegexValidator(regex='^[0-9]*$')])

