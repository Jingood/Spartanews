from rest_framework import serializers
from .models import Jjim

class JjimSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jjim
        fields = "__all__"