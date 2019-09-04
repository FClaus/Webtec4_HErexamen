from django.shortcuts import render
from django.http import JsonResponse
from .models import Overtreding
import json 

# Create your views here.

def overtreding(request, infractions_speed):
   json_data = open("./infractions.json")
   data1 = json.load(json_data)
   json_data.close()

   return render(request, 'index.html', {'data1': data1, 'infractions_speed': infractions_speed})

 

