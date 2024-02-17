from rest_framework import serializers
from .models import Patient


class PatientSerializer(serializers.ModelSerializer):
    birthDate = serializers.DateField(source='birth_date')

    class Meta:
        model = Patient
        fields = ['id', 'name', 'surname', 'sex', 'birthDate']
