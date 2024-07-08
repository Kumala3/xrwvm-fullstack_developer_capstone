from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class CarMake(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    year_established = models.IntegerField()
    country_of_origin = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class CarModel(models.Model):
    CAR_TYPES = [
        ("SEDAN", "Sedan"),
        ("SUV", "SUV"),
        ("WAGON", "Wagon"),
        ("SPORTS", "Sports"),
        ("COUPE", "Coupe"),
        ("CONVERTIBLE", "Convertible"),
        ("SUPERCAR", "Supercar"),
        ("HATCHBACK", "Hatchback"),
        ("MINIVAN", "Minivan"),
        ("PICKUP", "Pickup"),
        ("TRUCK", "Truck"),
        ("VAN", "Van"),
    ]

    dealer_id = models.IntegerField()
    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE, related_name='models')
    name = models.CharField(max_length=130)
    type = models.CharField(choices=CAR_TYPES, max_length=15, default="SUV")
    year = models.DateField(
        default=2023, validators=[MinValueValidator(2015), MaxValueValidator(2023)]
    )

    def __str__(self):
        return self.name
