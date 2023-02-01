from django.urls import path
from . import views

urlpatterns = [
    path('init/', views.initialize_elevator_system, name='initialize_elevator_system'),
    path('elevator_requests/<int:elevator_id>/', views.fetch_all_requests_for_elevator, name='fetch_all_requests_for_elevator'),
    path('next_destination/<int:elevator_id>/', views.fetch_next_destination_floor, name='fetch_next_destination_floor'),
    path('direction/<int:elevator_id>/', views.fetch_elevator_direction, name='fetch_elevator_direction'),
    path('request/<int:elevator_id>/', views.save_user_request, name='save_user_request'),
    path('status/<int:elevator_id>/', views.update_elevator_status, name='update_elevator_status'),
    path('door/<int:elevator_id>/', views.update_door_status, name='update_door_status'),
]
