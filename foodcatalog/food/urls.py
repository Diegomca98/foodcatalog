from . import views
from django.urls import path

urlpatterns = [
    path('', views.food, name="food"),
    path('item/<int:item_id>/', views.details, name="details"),
]