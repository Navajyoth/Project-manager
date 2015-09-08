from django.db import models
from django.db.models import Q


class TaskQuerySet(models.QuerySet):

    def active(self):
        items = self.exclude(status__in=('cancel', 'archive'))
        return items

    def filter_by_query_params(self, request):
        term = request.GET.get('term', None)
        status = request.GET.get('status', None)
        exclude = request.GET.get('exclude', None)
        project_ids = request.GET.get('projectid', None)
        user_ids = request.GET.get('userid', None)
        items = self

        if term:
            items = items.filter(Q(title__icontains=term) | Q(description__icontains=term))
        if status:
            status_list = [ s for s in status.split(',')]
            items = items.filter(status__in=status_list)
        if exclude:
            exclude_list = [e for e in exclude.split(',')]
            items = items.exclude(status__in=exclude_list)

        if project_ids:
            projects = [int(p) for p in project_ids if p.isdigit()]
            items = items.filter(project__in=projects)
        
        if user_ids:
            users = [int(u) for u in user_ids if u.isdigit()]
            items = items.filter(user__in=users)
        return items
