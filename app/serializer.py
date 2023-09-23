from rest_framework import serializers
from .models import *

class LegaleaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Legalease
        fields = ['prompt', 'result']
        