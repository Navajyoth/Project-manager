import json
from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import detail_route, list_route

from .models import Project, ProjectWork
from .serializers import ProjectSerializer, ProjectWorkSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    serializer_class = ProjectSerializer
    queryset = Project.objects.active()

    @list_route(methods=['GET'])
    def summary(self, request):
        result = []
        for project in self.queryset:
            status_list = list(project.tasks.values_list('status', flat=True))
            data = {
                'id': project.id,
                'name': project.name,
            }
            for status in status_list:
                data[status] = status_list.count(status)
            result.append(data)
        return Response(result)


class ProjectWorkViewSet(viewsets.ModelViewSet):
    serializer_class = ProjectWorkSerializer
    queryset = ProjectWork.objects.all()
