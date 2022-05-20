from rest_framework import serializers
from todo.models import Todo

class TodoSerializer(serializers.ModelSerializer): 
    #auto populated by app. User can't manipulate
    created = serializers.ReadOnlyField()
    completed = serializers.ReadOnlyField()

    class Meta:
        model = Todo
        fields = ['id', 'title', 'memo', 'created', 'completed']

class TodoToggleCompleteSerializer(serializers.ModelSerializer): 
    
    class Meta:
        model = Todo
        fields = ['id'] # Why need to show id?
        read_only_fields = ['title', 'memo', 'created', 'completed']