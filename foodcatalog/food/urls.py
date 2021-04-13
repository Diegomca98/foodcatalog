from . import views
from django.urls import path

urlpatterns = [
    path('', views.food, name="food"),
    path('item/<int:item_id>/', views.details, name="details"),
    path('add-item/', views.create_item, name="add"),
    path('update-item/<int:id>/', views.update_item, name="update"),
    path('delete-item/<int:id>/', views.delete_item, name="delete"),
]