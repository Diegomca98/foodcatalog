from . import views
from django.urls import path

urlpatterns = [
    #path('', views.food, name="food"),
    path('', views.FoodClassView.as_view(), name="food"),
    #path('item/<int:item_id>/', views.details, name="details"),
    path('item/<int:pk>/', views.DetailsClassView.as_view(), name="details"),
    #path('add-item/', views.create_item, name="add"),
    path('add-item/', views.CreateItem.as_view(), name="add"),
    path('update-item/<int:id>/', views.update_item, name="update"),
    path('delete-item/<int:id>/', views.delete_item, name="delete"),
]