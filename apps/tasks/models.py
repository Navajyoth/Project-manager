from django.db import models
from django.conf import settings

from model_utils.fields import StatusField
from model_utils import Choices

from apps.utils.models import AbstractTimestampModel
from apps.projects.models import Project
from apps.account.models import User
from apps.core.models import WorkType, Technology
from apps.utils.mail import MailSender
from .managers import TaskQuerySet


class Task(AbstractTimestampModel):
    STATUS = Choices('backlog', 'progress', 'rework', 'review', 'complete', 'cancel', 'archive')

    title = models.CharField(max_length=256)
    project = models.ForeignKey(Project, related_name='tasks')
    user = models.ForeignKey(User, related_name='tasks', null=True, blank=True)
    description = models.CharField(max_length=512, null=True, blank=True)
    status = StatusField(default=STATUS.backlog)
    # is_tested  = models.BooleanField()
    work_type = models.ForeignKey(WorkType, related_name='tasks', null=True, blank=True)
    estimated_time = models.DecimalField(max_digits=3, decimal_places=1, null=True, blank=True)
    actual_time = models.DecimalField(max_digits=3, decimal_places=1, null=True, blank=True)
    rework_time = models.DecimalField(max_digits=3, decimal_places=1, null=True, blank=True)
    technology = models.ForeignKey(Technology, related_name='tasks', null=True, blank=True)
    tag = models.CharField(max_length=128, null=True, blank=True)
    review_comments = models.CharField(max_length=1024, null=True, blank=True)
    priority = models.CharField(max_length=16, default='normal')
   
    objects = TaskQuerySet.as_manager()

    def __unicode__(self):
        return self.title

    def send_notification_assigned(self):
        url = settings.BASE_URL
        if not self.user:
            return
        context = {'task': self, 'url': url}
        mail = MailSender(self.user)
        mail.compose('[Assigned] ' + self.title, 'tasks/email/notify_task', context)
        mail.send_async()

    def send_review_notification(self):
        url = settings.BASE_URL + 'admin/tasks/task/%s/' % self.id
        if not self.project.owner:
            return
        context = {'task': self, 'url': url}
        mail = MailSender(self.project.owner)
        mail.compose('[Review] ' + self.title, 'tasks/email/notify_review', context)
        mail.send_async()

    def send_rework_notification(self):
        url = settings.BASE_URL
        if not self.user:
            return
        context = {'task': self, 'url': url}
        mail = MailSender(self.user)
        mail.compose('[Rework] ' + self.title, 'tasks/email/notify_rework', context)
        mail.send_async()

    def send_remider_notification(self):
        url = settings.BASE_URL
        if not self.user:
            return
        context = {'task': self, 'url': url}
        mail = MailSender(self.user)
        mail.compose('[Reminder] ' + self.title, 'tasks/email/notify_reminder', context)
        mail.send_async()

    class Meta:
        ordering = ('user', 'pk')


class Commit(models.Model):
    task = models.ForeignKey(Task, related_name='commits')
    url = models.URLField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return str(self.url)


class StatusLog(models.Model):
    task = models.ForeignKey(Task, related_name='status_logs')
    user = models.ForeignKey(User, related_name='status_logs', null=True, blank=True)
    status = models.CharField(max_length=16)
    time_stamp = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return "%s - %s(%s) - %s" % (self.user.name, self.task.title, self.status, self.time_stamp)

    class Meta:
        ordering = ('-pk',)

    @classmethod
    def create_status_log(cls, task):
        if task.user:
            user = task.user
        else:
            user = task.project.owner
        StatusLog.objects.create(task=task, status=task.status, user=task.user)
