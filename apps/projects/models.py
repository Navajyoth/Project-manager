from model_utils.fields import StatusField
from model_utils import Choices

from django.db import models
from apps.core.models import WorkType
from apps.account.models import User
from .managers import ProjectQuerySet


class Project(models.Model):
    STATUS = Choices('Green', 'Yellow', 'Red')

    name = models.CharField(max_length=64)
    owner = models.ForeignKey(User, null=True, blank=True)
    status = StatusField(default=STATUS.Green)
    is_active = models.BooleanField(default=True)

    objects = ProjectQuerySet.as_manager()

    def __unicode__(self):
        return self.name


class ProjectWork(models.Model):
    work_type = models.ForeignKey(WorkType, related_name='works')
    count = models.PositiveSmallIntegerField()
    rate = models.DecimalField(max_digits=20, decimal_places=2)
