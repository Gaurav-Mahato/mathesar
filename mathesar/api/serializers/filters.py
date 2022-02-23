from rest_framework import serializers


class FilterSerializer(serializers.Serializer):
    id = serializers.CharField()
    name = serializers.CharField()
    parameters = serializers.ListField(child=serializers.DictField())