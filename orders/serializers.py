from rest_framework import serializers
from typing import List

from .models import Order
from results.models import Result
from results.serializers import ShortResultSerializer


class ShortOrderSerializer(serializers.ModelSerializer):
    orderId = serializers.IntegerField(source='id')
    patientId = serializers.IntegerField(source='patient.id')
    resultIds = serializers.SerializerMethodField()

    def get_resultIds(self, order) -> List[int]:
        return list(Result.objects.filter(order=order).values_list("pk", flat=True))

    class Meta:
        model = Order
        fields = ['orderId', 'patientId', 'resultIds', ]


class LongOrderSerializer(serializers.ModelSerializer):
    orderId = serializers.CharField(source='id')
    results = ShortResultSerializer(source='result_set', many=True)

    class Meta:
        model = Order
        fields = ['orderId', 'results']
