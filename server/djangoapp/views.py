from django.http import HttpRequest
from django.contrib.auth.models import User
from django.contrib.auth import logout

from django.http import JsonResponse
from django.contrib.auth import login, authenticate
import logging
import json
from django.views.decorators.csrf import csrf_exempt
from .populate import initiate
from .restapis import analyze_review_sentiments, get_request

from .models import CarMake, CarModel

# Get an instance of a logger
logger = logging.getLogger(__name__)


def get_cars(request):
    count = CarMake.objects.count()

    if count == 0:
        initiate()  # Call initiate to populate data
        count = CarMake.objects.count()  # Recheck count after initiation

    car_models = CarModel.objects.select_related("car_make").all()
    cars = []
    for car_model in car_models:
        cars.append({"CarModel": car_model.name, "CarMake": car_model.car_make.name})

    return JsonResponse({"CarModels": cars})


# Create a `login_request` view to handle sign in request
@csrf_exempt
def login_user(request: HttpRequest):
    if request.method != "POST":
        return JsonResponse({"error": "POST request required."}, status=400)
    # Get username and password from request.POST dictionary
    data = json.loads(request.body)
    username = data.get("userName")
    password = data.get("password")
    # Try to check if provide credential can be authenticated
    user = authenticate(username=username, password=password)
    if user is not None:
        # If user is valid, call login method to login current user
        login(request, user)
        data = {"userName": username, "status": "Authenticated"}
        return JsonResponse(data)
    return JsonResponse(
        {"error": "We're having issue right now, contact our dev team"}, status=400
    )


# Create a `logout_request` view to handle sign out request
def logout_request(request: HttpRequest):
    logout(request)
    data = {"username": "", "status": "Logged out"}
    return JsonResponse(data)


# Create a `registration` view to handle sign up request
@csrf_exempt
def registration(request: HttpRequest):
    if request.method == "POST":
        data = json.loads(request.body)
        username = data.get("userName")
        password = data.get("password")
        firstname = data.get("firstName")
        lastname = data.get("lastName")
        email = data.get("email")

        if not username or not password or not firstname or not lastname or not email:
            return JsonResponse({"error": "All parameters are required"}, status=400)
        if User.objects.filter(username=username):
            return JsonResponse({"error": "Already Registered"}, status=400)

        user = User.objects.create(
            username=username,
            first_name=firstname,
            last_name=lastname,
            email=email,
        )
        user.set_password(password)
        user.save()
        if user:
            login(request, user)
            data = {
                "userName": username,
                "message": "User registered successfully",
                "status": "Authenticated",
            }
            return JsonResponse(data, status=201)
        else:
            JsonResponse({"error": f"Cannot register user: {username}"}, status=400)
    return JsonResponse(
        {"error": "This endpoint supports only POST requests"}, status=405
    )


# # Update the `get_dealerships` view to render the index page with
# a list of dealerships
def get_dealerships(request: HttpRequest, state="All"):
    if state == "All":
        endpoint = "/fetchDealers"
    else:
        endpoint = f"/fetchDealers/{state}"
    dealerships = get_request(endpoint)
    if dealerships.status_code == 200:
        dealerships = dealerships.json()
    return JsonResponse({"status": 200, "dealers": dealerships})


# Create a `get_dealer_reviews` view to render the reviews of a dealer
def get_dealer_reviews(request: HttpRequest, dealer_id: int):
    pass


# Create a `get_dealer_details` view to render the dealer details
def get_dealer_details(request: HttpRequest, dealer_id: int):
    pass


# Create a `add_review` view to submit a review
def add_review(request: HttpRequest):
    pass
