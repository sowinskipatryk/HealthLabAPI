from rest_framework import serializers
from .models import Order
from results.models import Result


class ShortOrderSerializer(serializers.ModelSerializer):
    orderId = serializers.IntegerField(source='id')

    class Meta:
        model = Order
        fields = ['orderId', ]


class LongOrderSerializer(serializers.ModelSerializer):
    orderId = serializers.IntegerField(source='id')
    patientId = serializers.IntegerField(source='patient.id')
    resultIds = serializers.SerializerMethodField()

    def get_resultIds(self, order):
        return list(Result.objects.filter(order=order).values_list("pk", flat=True))

    class Meta:
        model = Order
        fields = ['orderId', 'patientId', 'resultIds', ]
