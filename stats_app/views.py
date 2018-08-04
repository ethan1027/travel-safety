from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from stats_app.models import Gunshot
import json
from django.core.serializers.json import DjangoJSONEncoder

from .serializers import StateSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import  status
from .models import State, City
from .serializers import StateSerializer, CitySerializer, GunshotSerializer
import math
import decimal
# Create your views here.

def index(request):
    all_gunshots = Gunshot.objects.filter(lat__isnull=False).exclude(lat=0.0).filter(lng__isnull=False).exclude(lng=0.0).exclude(lat=decimal.Decimal('NaN')).exclude(lng=decimal.Decimal('NaN'))
    location_dict = list(all_gunshots.values('lat','lng'))
    return render(request,'index.html', {"location_dict": json.dumps(location_dict, cls= DjangoJSONEncoder)})

class StateList(APIView):
    def get(self, request):
        states = State.objects.all()
        serializer = StateSerializer(states, many=True)
        return Response(serializer.data)

class CityList(APIView):
    def get(self, request):
        cities = City.objects.all()
        serializer = CitySerializer(cities, many=True)
        return Response(serializer.data)

class GunshotList(APIView):
    def get(self, request):
        gunshots = Gunshot.objects.all()
        serializer = GunshotSerializer(gunshots, many=True)
        return JsonResponse(serializer.data, safe=False)
