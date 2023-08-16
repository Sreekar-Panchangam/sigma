from rest_framework import serializers
from .models import *
from workorder.models import HoistWorkOrder

class InformationSheetAddSerializer(serializers.ModelSerializer):
    class Meta:
        model = HoistInformationSheet
        fields = '__all__'

