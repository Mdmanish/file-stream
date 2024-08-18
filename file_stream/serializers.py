from rest_framework import serializers

class FileCreateSerializer(serializers.Serializer):
    filename = serializers.CharField(max_length=100)
    content = serializers.CharField()
