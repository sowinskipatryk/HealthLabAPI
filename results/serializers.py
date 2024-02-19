from rest_framework import serializers
from .models import Result


class ShortResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = Result
        fields = ['name', 'value', 'reference']


class LongResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = Result
        fields = ['id', 'name', 'value', 'reference']
