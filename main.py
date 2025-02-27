from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

def index(request):
    # Render the  index page
    return render(request, 'floodapp/index.html')  


@csrf_exempt  

def analyze(request):
    if request.method == 'POST':

        # Get the values from the form
        rainfall = request.POST.get('rainfall') == 'on'
        water_levels = request.POST.get('waterLevels') == 'on'
        roads = request.POST.get('roads') == 'on'
        clean_water = request.POST.get('cleanWater') == 'on'
        isolation = request.POST.get('isolation') == 'on'

        message = ""
        alert_type = "low-risk"  # Default value

        # Logic to determine the alert level
        if rainfall and water_levels:
            message = "RED ALERT: Immediate evacuation is recommended! Seek higher ground.\n"
            alert_type = "high-risk"  # Critical condition
        elif rainfall or water_levels:
            message = "ORANGE ALERT: Be prepared for evacuation and stay informed on weather updates.\n"
            alert_type = "moderate-risk"  # Moderate condition
        else:
            message = "GREEN ALERT: No immediate danger detected, stay informed.\n"
            alert_type = "low-risk"  # Safe condition

        # Additional messages based on other conditions
        if not clean_water:
            message += " Use purification tablets or boiled water.\n"
             
        if roads:
            message += " Avoid flooded roads and seek alternative routes.\n"

        if isolation:
            message += " Contact emergency services for assistance at '112' or '115'\n"

        # to Return the response with both message and alertType
        return JsonResponse({'message': message, 'alertType': alert_type})

    else:
        return JsonResponse({'error': 'Invalid request method'}, status=400)
