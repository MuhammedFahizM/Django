from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'   # or ['name'] for single data





from rest_framework import serializers
from .models import Task

class TaskSerialzer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'task_name', 'completed']