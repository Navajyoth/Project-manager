from django.contrib import admin

from .models import Task, Commit


class CommitInline(admin.StackedInline):
    model = Commit


class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'status')
    list_filter = ('status', 'project', 'user')
    search_fields = ('title', )
    inlines = [CommitInline, ]

admin.site.register(Task, TaskAdmin)
