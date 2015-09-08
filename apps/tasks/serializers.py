from rest_framework import serializers

from apps.utils.fields import get_fields_and_values, get_changed_fields
from .models import Task, Commit, StatusLog


class MiniCommitSerializer(serializers.ModelSerializer):

    class Meta:
        model = Commit
        fields = ('id', 'url')


class TaskSerializer(serializers.ModelSerializer):
    commits = MiniCommitSerializer(many=True, read_only=True)
    project_name = serializers.CharField(source="project.name", read_only=True)

    class Meta:
        model = Task
        fields = (
            'id', 'title', 'description', 'user', 'status', 'project', 'project_name', 'work_type',
            'estimated_time', 'actual_time', 'rework_time', 'technology', 'tag', 'review_comments', 'priority', 'commits')

    def create(self, validated_data):
        item = super(TaskSerializer, self).create(validated_data)
        user = item.user

        StatusLog.create_status_log(item)
        item.send_notification_assigned()
        return item

    def update(self, instance, validated_data):
        initial_data = get_fields_and_values(instance)
        item = super(TaskSerializer, self).update(instance, validated_data)
        user = item.user
        status = validated_data['status']
        project_owner = validated_data['project'].owner

        if status == 'review':
            item.send_review_notification()
        elif status == 'rework':
            item.send_rework_notification()

        updated_data = get_fields_and_values(instance)
        fields = get_changed_fields(initial_data, updated_data)

        if 'user' in fields:
            item.send_notification_assigned()
        if 'status' in fields:
            StatusLog.create_status_log(item)

        return item


class CommitSerializer(serializers.ModelSerializer):
    task_name = serializers.CharField(source="task.title", read_only=True)

    class Meta:
        model = Commit
        fields = ('id', 'task', 'task_name', 'url', 'created')


class TaskMiniSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Task
        fields = ('id', 'title', 'status', 'user')


class StatusLogSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source='user.name')
    task = serializers.CharField(source='task.title')

    class Meta:
        model = StatusLog
        fields = ('id', 'user', 'task', 'status', 'time_stamp')
        read_only_fields = fields
