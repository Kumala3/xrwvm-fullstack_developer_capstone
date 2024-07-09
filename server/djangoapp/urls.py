from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from .views import (
    login_user,
    logout_request,
    registration,
    get_cars,
    get_dealerships,
    get_dealer_details,
    get_dealer_reviews,
    get_reviews,
    add_review,
)

app_name = "djangoapp"
urlpatterns = [
    path("login", view=login_user, name="login"),
    path("logout", view=logout_request, name="logout"),
    path("register", view=registration, name="register"),
    path("dealers/", view=get_dealerships, name="dealers"),
    path("dealers/<str:state>", view=get_dealerships, name="dealers_by_state"),
    path(
        "dealers_details/<int:dealer_id>",
        view=get_dealer_details,
        name="dealer_details",
    ),
    path("reviews", view=get_reviews, name="reviews"),
    path(
        "reviews/dealer/<int:dealer_id>",
        view=get_dealer_reviews,
        name="dealer_reviews_by_dealer_id",
    ),
    path("get_cars/", view=get_cars, name="get_cars"),
    path("add_review", view=add_review, name="add_review"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
