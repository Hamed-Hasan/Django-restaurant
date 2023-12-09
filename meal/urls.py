from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_item, name='show_item'),
    path('<str:item_id>/', views.show_item_details, name='show_item_details'),
]
