from django.shortcuts import render
import requests
from django.http import JsonResponse

# Create your views here.
# labs/views.py
# import requests
# from django.http import JsonResponse

# Replace this with the actual API endpoint for fetching labs data
EXTERNAL_API_URL = "https://api.example.com/labs"

def search_labs(request):
    city = request.GET.get('city', '').lower()  # Get 'city' from the query string

    try:
        # Make an API call to fetch lab data
        response = requests.get(EXTERNAL_API_URL)
        response.raise_for_status()  # Raise an error for bad status codes (4xx, 5xx)

        # Parse the JSON response from the API
        labs_data = response.json()

        # Filter labs based on city query
        results = [lab for lab in labs_data if city in lab['location'].lower()]

        return JsonResponse({"labs": results})

    except requests.RequestException as e:
        # Handle API call errors, e.g., network issues, bad response, etc.
        return JsonResponse({"error": str(e)}, status=500)
