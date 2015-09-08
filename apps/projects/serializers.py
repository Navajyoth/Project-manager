from rest_framework import serializers

from .models import Project, ProjectWork


class ProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Project
        fields = ('name', 'id', 'owner', 'status', 'is_active')


class ProjectWorkSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProjectWork
        fields = ('work_type', 'count', 'rate', 'id')
