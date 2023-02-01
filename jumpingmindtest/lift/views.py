from django.http import JsonResponse
from .models import Elevator, ElevatorRequest

def initialize_elevator_system(request, number_of_elevators=2):
    for i in range(number_of_elevators):
        Elevator.objects.create(elevator_id=i)
    return JsonResponse({'message': f'Elevator system initialized with {number_of_elevators} elevators'})

def fetch_all_requests_for_elevator(request, elevator_id):
    elevator = Elevator.objects.get(elevator_id=elevator_id)
    requests = ElevatorRequest.objects.filter(elevator=elevator)
    return JsonResponse({'requests': [request.floor for request in requests]})

def fetch_next_destination_floor(request, elevator_id):
    elevator = Elevator.objects.get(elevator_id=elevator_id)
    requests = ElevatorRequest.objects.filter(elevator=elevator).order_by('floor')
    if requests:
        return JsonResponse({'next_destination': requests[0].floor})
    return JsonResponse({'next_destination': None})

def fetch_elevator_direction(request, elevator_id):
    elevator = Elevator.objects.get(elevator_id=elevator_id)
    requests = ElevatorRequest.objects.filter(elevator=elevator).order_by('floor')
    if requests:
        if elevator.current_floor < requests[0].floor:
            return JsonResponse({'direction': 'up'})
        return JsonResponse({'direction': 'down'})
    return JsonResponse({'direction': None})

def save_user_request(request, elevator_id, floor):
    elevator = Elevator.objects.get(elevator_id=elevator_id)
    ElevatorRequest.objects.create(elevator=elevator, floor=floor)
    return JsonResponse({'message': f'Request for floor {floor} saved for elevator {elevator_id}'})

def update_elevator_status(request, elevator_id, status):
    elevator = Elevator.objects.get(elevator_id=elevator_id)
    elevator.status = status
    elevator.save()
    return JsonResponse({'message': f'Elevator {elevator_id} status updated to {status}'})

def update_door_status(request, elevator_id, status):
    elevator = Elevator.objects.get(elevator_id=elevator_id)
    elevator.door_status = status
    elevator.save()
    return JsonResponse({'message': f'Elevator {elevator_id} door status updated to {status}'})
