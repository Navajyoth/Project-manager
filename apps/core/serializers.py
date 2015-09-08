from rest_framework import serializers

from .models import WorkType, Technology


class WorkTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = WorkType
        fields = ('name',)


class TechnologySerializer(serializers.ModelSerializer):

    class Meta:
        model = Technology
        fields = ('name', 'is_deleted')
