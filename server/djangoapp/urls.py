from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from .views import login_user, logout_request, registration, get_dealerships

app_name = 'djangoapp'
urlpatterns = [
    path('login', view=login_user, name='login'),
    path('logout', view=logout_request, name='logout'),
    path('register', view=registration, name='register'),
    path('dealerships/', view=get_dealerships, name='get_dealerships'),

    # path for dealer reviews view

    # path for add a review view

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
