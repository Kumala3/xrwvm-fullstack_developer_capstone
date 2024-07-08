from .models import CarMake, CarModel


def initiate():
    car_make_data = [
        {
            "name": "NISSAN",
            "description": "Great cars. Japanese technology",
            "year_established": 1933,
            "country_of_origin": "Japan",
        },
        {
            "name": "Mercedes",
            "description": "Great cars. German technology",
            "year_established": 1926,
            "country_of_origin": "Germany",
        },
        {
            "name": "Audi",
            "description": "Great cars. German technology",
            "year_established": 1909,
            "country_of_origin": "Germany",
        },
        {
            "name": "Kia",
            "description": "Great cars. Korean technology",
            "year_established": 1944,
            "country_of_origin": "South Korea",
        },
        {
            "name": "Toyota",
            "description": "Great cars. Japanese technology",
            "year_established": 1937,
            "country_of_origin": "Japan",
        },
        {
            "name": "BMW",
            "description": "Great cars. German technology",
            "year_established": 1916,
            "country_of_origin": "Germany",
        },
        {
            "name": "Ford",
            "description": "Great cars. American technology",
            "year_established": 1903,
            "country_of_origin": "United States",
        },
        {
            "name": "Honda",
            "description": "Great cars. Japanese technology",
            "year_established": 1948,
            "country_of_origin": "Japan",
        },
        {
            "name": "Chevrolet",
            "description": "Great cars. American technology",
            "year_established": 1911,
            "country_of_origin": "United States",
        },
        {
            "name": "Volkswagen",
            "description": "Great cars. German technology",
            "year_established": 1937,
            "country_of_origin": "Germany",
        },
    ]

    car_make_instances = []
    for data in car_make_data:
        car_make_instances.append(
            CarMake.objects.create(
                name=data["name"],
                description=data["description"],
                year_established=data["year_established"],
                country_of_origin=data["country_of_origin"],
            )
        )

    # Create CarModel instances with the corresponding CarMake instances
    car_model_data = [
        {
            "name": "Pathfinder",
            "type": "SUV",
            "year": 2023,
            "car_make": car_make_instances[0],
        },
        {
            "name": "Qashqai",
            "type": "SUV",
            "year": 2023,
            "car_make": car_make_instances[0],
        },
        {
            "name": "XTRAIL",
            "type": "SUV",
            "year": 2023,
            "car_make": car_make_instances[0],
        },
        {
            "name": "A-Class",
            "type": "SUV",
            "year": 2023,
            "car_make": car_make_instances[1],
        },
        {
            "name": "C-Class",
            "type": "SUV",
            "year": 2023,
            "car_make": car_make_instances[1],
        },
        {
            "name": "E-Class",
            "type": "SUV",
            "year": 2023,
            "car_make": car_make_instances[1],
        },
        {"name": "A4", "type": "SUV", "year": 2023, "car_make": car_make_instances[2]},
        {"name": "A5", "type": "SUV", "year": 2023, "car_make": car_make_instances[2]},
        {"name": "A6", "type": "SUV", "year": 2023, "car_make": car_make_instances[2]},
        {
            "name": "Sorrento",
            "type": "SUV",
            "year": 2023,
            "car_make": car_make_instances[3],
        },
        {
            "name": "Carnival",
            "type": "SUV",
            "year": 2023,
            "car_make": car_make_instances[3],
        },
        {
            "name": "Cerato",
            "type": "Sedan",
            "year": 2023,
            "car_make": car_make_instances[3],
        },
        {
            "name": "Corolla",
            "type": "Sedan",
            "year": 2023,
            "car_make": car_make_instances[4],
        },
        {
            "name": "Camry",
            "type": "Sedan",
            "year": 2023,
            "car_make": car_make_instances[4],
        },
        {
            "name": "Kluger",
            "type": "SUV",
            "year": 2023,
            "car_make": car_make_instances[4],
        },
        {
            "name": "Fiesta",
            "type": "Hatchback",
            "year": 2023,
            "car_make": car_make_instances[6],
        },
        {
            "name": "Mustang",
            "type": "Coupe",
            "year": 2023,
            "car_make": car_make_instances[6],
        },
        {
            "name": "Focus",
            "type": "Sedan",
            "year": 2023,
            "car_make": car_make_instances[6],
        },
        {
            "name": "Civic",
            "type": "Sedan",
            "year": 2023,
            "car_make": car_make_instances[7],
        },
        {
            "name": "Accord",
            "type": "Sedan",
            "year": 2023,
            "car_make": car_make_instances[7],
        },
        {
            "name": "CR-V",
            "type": "SUV",
            "year": 2023,
            "car_make": car_make_instances[7],
        },
        {
            "name": "Camaro",
            "type": "Coupe",
            "year": 2023,
            "car_make": car_make_instances[8],
        },
        {
            "name": "Silverado",
            "type": "Truck",
            "year": 2023,
            "car_make": car_make_instances[8],
        },
    ]

    for data in car_model_data:
        CarModel.objects.create(
            name=data["name"],
            car_make=data["car_make"],
            type=data["type"],
            year=data["year"],
        )
