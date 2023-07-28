from rest_framework import serializers

class wifiModeSerializer(serializers.Serializer):
    user = serializers.CharField(max_length=100)