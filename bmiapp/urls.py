from django.urls import URLPattern, path
from .views import home

urlpatterns = [
    path('', home, name="home")

]