from rest_framework import serializers
from .models import User, UserTechnology


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('name', 'email', 'id', 'is_manager', 'is_visible')


class UserTechnologySerializer(serializers.ModelSerializer):

    class Meta:
        model = UserTechnology
        fields = ('user', 'technology')
