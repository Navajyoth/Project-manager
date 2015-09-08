from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import list_route, detail_route

from .models import Task, Commit, StatusLog
from .serializers import TaskSerializer, CommitSerializer, TaskMiniSerializer, StatusLogSerializer


class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    queryset = Task.objects.prefetch_related('commits').all()

    def list(self, request):
        # self.queryset = Task.objects.select_related('user').active().exclude(status="complete")
        tasks = Task.objects.all().filter_by_query_params(request)
        detail_str = request.GET.get('detail', True)
        if detail_str:
            slz = TaskSerializer(tasks, many=True)
        else:
            slz = TaskMiniSerializer(tasks, many=True)
        return Response(slz.data)

    @list_route(methods=['GET'])
    def user(self, request):
        id_str = request.GET.get('userid', None)
        if id_str.isdigit():
            tasks = self.queryset.filter(user__pk=int(id_str))
        else:
            tasks = self.queryset.filter(user=request.user)
        slz = TaskSerializer(tasks, many=True)
        return Response(slz.data)

    @detail_route(methods=['GET'])
    def notify(self, request, pk=None):
        task = self.get_object()
        task.send_remider_notification()
        return Response('Reminder notification is sent.')

class CommitViewSet(viewsets.ModelViewSet):
    serializer_class = CommitSerializer
    queryset = Commit.objects.all()


class StatusLogViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = StatusLogSerializer
    queryset = StatusLog.objects.all()
    paginate_by = 10
