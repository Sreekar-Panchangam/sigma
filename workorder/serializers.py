from rest_framework import serializers
from .models import *

class HoistWorkOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = HoistWorkOrder
        fields = "__all__"