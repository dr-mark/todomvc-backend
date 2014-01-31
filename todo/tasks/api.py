from tastypie.resources import ModelResource
from tasks.models import Task


class TaskResource(ModelResource):
    class Meta:
        queryset = Task.objects.all()
        resource_name = 'task'
