from rest_framework import serializers
from task_list.models import Task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('id', 'name', 'about', 'image', 'create_date', 'expiration_date', 'status',)
