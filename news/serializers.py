from rest_framework import serializers
from accounts.models import User
from .models import News

class NewsSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), default = serializers.CurrentUserDefault())
    class Meta:
        model = News
        fields = "__all__"
        read_only_fields = ["author"]