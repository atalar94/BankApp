from rest_framework import serializers
from .models import CustomUser, Sube


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = "__all__"

class SubeSerializer (serializers.ModelSerializer):
    class Meta:
        model = Sube
        fields = "__all__"