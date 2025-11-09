from django.shortcuts import render

# Create your views here.

from rest_framework.decorators import api_view
from .models import Book
from .serializers import BookSerializer
from rest_framework.response import Response

# creating API VIEWS with DRF


@api_view(['GET'])
def get_books(request):
    books = Book.objects.all()
    serializer = BookSerializer(books, many = True)
    return Response(serializer.data)

