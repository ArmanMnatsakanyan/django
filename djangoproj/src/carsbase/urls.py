from django.urls import path
from .views import cars_list_view, car_create_view, car_delete_view, car_detail_view
#from carsbase.views import home_view

app_name = 'carsbase'

urlpatterns = [
    path('create/', car_create_view, name='create'),
    path('<int:id>/', car_detail_view, name='car'),
    path('<int:id>/delete/', car_delete_view, name='car-delete'),
    path('', cars_list_view, name='cars'),
]
