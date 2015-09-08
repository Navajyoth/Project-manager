from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from rest_framework import viewsets

from .models import WorkType, Technology
from .serializers import WorkTypeSerializer, TechnologySerializer


class WorkTypeViewSet(viewsets.ModelViewSet):
    serializer_class = WorkTypeSerializer
    queryset = WorkType.objects.all()


class TechnologyViewSet(viewsets.ModelViewSet):
    serializer_class = TechnologySerializer
    queryset = Technology.objects.all()


@login_required
def home_view(request):
    template = "index.html"
    return render(request, template)
