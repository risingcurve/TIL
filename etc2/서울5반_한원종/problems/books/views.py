from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.shortcuts import get_object_or_404, get_list_or_404

from .serializers import BookListSerializer, BookSerializer, CommentSerializer
from .models import Book, Comment


@api_view(['GET', 'POST'])
def book_list(request):
    # Q 1.
    if request.method == 'GET':
        books = Book.objects.all()
        serializer = BookListSerializer(books, many=True)
        return Response(serializer.data)

        # books = get_list_or_404(Book)
        # serializer = BookListSerializer(books, many=True)
        # return Response(serializer.data)

    # Q 2.
    if request.method == 'POST':
        books = Book.objects.all()
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)



@api_view(['GET', 'DELETE', 'PUT'])
def book_detail(request, book_pk):
    # Q 3.
    if request.method == 'GET':
        book = book.objects.get(request, pk=book_pk)
        serializer = BookSerializer(raise_exception=True)
        return Response(serializer.data, status=status.HTTP_404)
        
    # Q 4.
    if request.method == 'DELETE':
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    # Q 5.
    if request.method == 'PUT':
        serializer = BookSerializer(book, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)



@api_view(['GET'])
def comment_list(request):
    # Q 7.
    if request.method == 'GET':
        comments = get_list_or_404(Comment)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)
    


@api_view(['POST'])
def comment_create(request, book_pk):
    # Q 8.
    comments = get_object_or_404(request, pk=book_pk)
    serializer = CommentSerializer(comments, many=True)
    return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'DELETE'])
def comment_detail(request, comment_pk):
    # Q 9.
        if request.method == 'GET':
            comment = get_object_or_404(Comment, pk=comment_pk)
            return Response(status=status.HTTP_404_NOT_FOUND)
    # Q 10.
        if request.method == 'DELETE':
            comment.delete()
            return Response(status=status.HTTP_404_NOT_FOUND)

