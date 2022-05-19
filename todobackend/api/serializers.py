from rest_framework import serializers
from todo.models import Todo

class Todo(serializers.ModelSerializer): 
    #auto populated by app. User can't manipulate
    created = serializers.ReadOnlyField()
    completed = serializers.ReadOnlyField()

    class Meta:
        model = Todo
        fields = ['id', 'title', 'memo', 'created', 'completed']