from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='food_home_page'),
    path('locations/',views.locations, name='locations_page'),
    path('locations/retail/',views.retail, name='retail_page'),
    path('locations/meal_plan/',views.meal_plan, name='meal_plan_page'),
    path('locations/meal_exchange/',views.meal_exchange, name='meal_exchange_page')
]