from django.db import models


class WorkType(models.Model):
    name = models.CharField(max_length=64)

    def __unicode__(self):
        return self.name


class Technology(models.Model):
    name = models.CharField(max_length=64)
    is_deleted = models.BooleanField(default=False)

    def __unicode__(self):
        return self.name
