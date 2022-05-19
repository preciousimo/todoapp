from django.shortcuts import render
from rest_framework import generics
from .serializers import TodoSerializer
from todo.models import Todo

# Create your views here.
class TodoListCreate(generics.ListCreateAPIView):
    # ListAPIView requires two mandatory attributes, serializer_class and queryset.
    # We specify TodoSerializer which we have earlier implemented
    serializer_class = TodoSerializer

    def get_queryset(self):
        user = self.request.user
        return Todo.objects.filter(user=user).order_by('-created')

    #perform_create acts as a hook which is called before the instance is created in the database.
    def perform_create(self, serializer):
        #serializer holds a django model
        serializer.save(user=self.request.user)


