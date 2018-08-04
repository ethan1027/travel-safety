from rest_framework import serializers
from .models import State
from .models import City
from .models import Gunshot

class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = State
        fields = '__all__'

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'

class GunshotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gunshot
        fields = '__all__'