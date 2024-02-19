from rest_framework import serializers

from .models import Patient
from orders.serializers import LongOrderSerializer


class PatientSerializer(serializers.ModelSerializer):
    birthDate = serializers.DateField(source='birth_date')
    sex = serializers.SerializerMethodField()

    class Meta:
        model = Patient
        fields = ['id', 'name', 'surname', 'sex', 'birthDate']

    def get_sex(self, obj) -> str:
        long_sex = obj.sex
        short_sex = long_sex[0]
        return short_sex


class PatientProfileSerializer(serializers.ModelSerializer):
    patient = PatientSerializer(source='*')
    orders = LongOrderSerializer(source='order_set', many=True)

    class Meta:
        model = Patient
        fields = ['patient', 'orders']
