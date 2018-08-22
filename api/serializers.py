from rest_framework import serializers
from .models import Patient


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ('id', 'firstname', 'lastname', 'email', 'city', 'address', 'phone', 'gender', 'age')
