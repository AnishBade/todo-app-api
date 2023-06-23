from rest_framework import generics


from .models import Todo

from .serializers import TodoSerializer

class ListTodo(generics.ListAPIView):
    queryset = Todo.objects.all()
    # lseriaizer_class = TodoSerializer
    
    def get_serializer_class(self):
        return TodoSerializer


class DetailTodo(generics.RetrieveAPIView):
    queryset = Todo.objects.all()
    # serializer_class = TodoSerializer

    def get_serializer_class(self):
        return TodoSerializer