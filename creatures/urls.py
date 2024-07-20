from django.urls import path
from . import views

urlpatterns = [
    path("", views.creature_list),
    path("<int:id>/", views.creature_detail),
]
