from rest_framework import serializers
from .models import *

class HoistWorkOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = HoistWorkOrder
        fields = "__all__"

from rest_framework import serializers
from .models import HoistWorkOrder

class HoistWorkOrderAddSerializer(serializers.ModelSerializer):
    class Meta:
        model = HoistWorkOrder
        fields = '__all__'  # Or specify the fields you want to include

    # Ensure the customer field is set up correctly
    customer = serializers.PrimaryKeyRelatedField(queryset=Customer.objects.all())

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = "__all__"
