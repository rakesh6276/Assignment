from rest_framework import serializers
from .models import Pitches

class PitchesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pitches
        fields = '__all__'

class PitchesSerializerget(serializers.ModelSerializer):
    class Meta:
        model = Pitches
        fields = ('name', 'brand', 'sku_code', 'package')