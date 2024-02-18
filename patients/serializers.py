from rest_framework import serializers
from .models import Patient
from orders.serializers import LongOrderSerializer
from orders.models import Order


class PatientSerializer(serializers.ModelSerializer):
    birthDate = serializers.DateField(source='birth_date')

    class Meta:
        model = Patient
        fields = ['id', 'name', 'surname', 'sex', 'birthDate']


class PatientProfileSerializer(serializers.ModelSerializer):
    birthDate = serializers.DateField(source='birth_date')

    class Meta:
        model = Patient
        fields = ['id', 'name', 'surname', 'sex', 'birthDate']

    def to_representation(self, instance):
        data = super().to_representation(instance)
        orders = Order.objects.filter(patient=instance)
        order_serializer = LongOrderSerializer(orders, many=True)
        return {
            "patient": {
                "id": data['id'],
                "name": data['name'],
                "surname": data['surname'],
                "sex": data['sex'][0],
                "birthDate": data['birthDate'],
            },
            "orders": order_serializer.data
        }
