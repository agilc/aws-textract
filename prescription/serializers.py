from rest_framework import serializers
from .models import Prescriptions

class PrescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prescriptions
        fields = '__all__'