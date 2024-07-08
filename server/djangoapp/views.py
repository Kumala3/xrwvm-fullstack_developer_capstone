from django.shortcuts import render
from django.http import HttpRequest, HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import logout
from django.contrib.auth.hashers import make_password
from django.contrib import messages
from datetime import datetime

from django.http import JsonResponse
from django.contrib.auth import login, authenticate
import logging
import json
from django.views.decorators.csrf import csrf_exempt
from .populate import initiate


# Get an instance of a logger
logger = logging.getLogger(__name__)


# Create a `login_request` view to handle sign in request
@csrf_exempt
def login_user(request: HttpRequest):
    if request.method != "POST":
        return JsonResponse({"error": "POST request required."}, status=400)
    # Get username and password from request.POST dictionary
    data = json.loads(request.body)
    username = data["userName"]
    password = data["password"]
    # Try to check if provide credential can be authenticated
    user = authenticate(username=username, password=password)
    print(user)
    if user is not None:
        # If user is valid, call login method to login current user
        login(request, user)
        data = {"userName": username, "status": "Authenticated"}
        print(JsonResponse(data), status=200)
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
        username = data["userName"]
        password = data["password"]
        firstname = data["firstName"]
        lastname = data["lastName"]
        email = data["email"]

        if not username or not password or not firstname or not lastname or not email:
            return JsonResponse({"error": "All parameters are required"}, status=400)
        if User.objects.filter(username=username):
            return JsonResponse({"error": "Already Registered"}, status=400)

        user = User.objects.create(
            username=username,
            password=password,
            first_name=firstname,
            last_name=lastname,
            email=email,
        )
        print(user)
        login(request, user)
        data = {
            "userName": username,
            "message": "User registered successfully",
            "status": "Authenticated",
        }
        return JsonResponse(data, status=201)
    return JsonResponse(
        {"error": "This endpoint supports only POST requests"}, status=405
    )


# # Update the `get_dealerships` view to render the index page with
# a list of dealerships
def get_dealerships(request: HttpRequest):
    pass


# Create a `get_dealer_reviews` view to render the reviews of a dealer
def get_dealer_reviews(request: HttpRequest, dealer_id: int):
    pass


# Create a `get_dealer_details` view to render the dealer details
def get_dealer_details(request: HttpRequest, dealer_id: int):
    pass


# Create a `add_review` view to submit a review
def add_review(request: HttpRequest):
    pass
