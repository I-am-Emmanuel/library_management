from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Book, Member, PhysicalBook
from .serializer import BookSerializer, MemberSerializer
from rest_framework import generics, viewsets, status
from django.db import transaction
from django.shortcuts import get_object_or_404
# from django_filters.rest_framework import DjangoFilterBackend as DFB
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend as DFB


class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [DFB]
    filterset_fields = ['title', 'authors']

    def get_serializer_context(self):
        return {'request': self.request}


    def delete(self, request, pk):
        book = get_object_or_404(Book, pk=pk)
        if book.physical_books.count() > 0:
            return Response({'error': 'This book cannot be deleted. It has been borrowed by a user'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    
# class MemberViewSet(viewsets.ModelViewSet):
#     queryset = Member.objects.all()
#     serializer_class = MemberSerializer
#     filter_backends = [DFB]
#     filterset_fields = ['memberId', 'name']
    

#     @action(detail=True, methods=['POST'])
#     def borrow_physical_book(self, request, pk=None):
#         member = get_object_or_404(Member, pk=pk)
#         book_id = request.data.get('book_id')

#         try:
#             with transaction.atomic():
#                 book = get_object_or_404(PhysicalBook, id=book_id, isAvailable=True)
#                 book.isAvailable = False
#                 book.save()
#                 member.borrowed_books = book
#                 member.save()

#             return Response({'message': 'Physical book borrowed successfully.'})
#         except PhysicalBook.DoesNotExist:
#             return Response({'error': 'Physical book not found.'}, status=status.HTTP_404_NOT_FOUND)

class MemberViewSet(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer
    filter_backends = [DFB]
    filterset_fields = ['memberId']


    @action(detail=True, methods=['POST']) 
    def borrow_physical_book(self, request, pk=None):
        member = get_object_or_404(Member, pk=pk)
        book_id = request.data.get('book_id')

        try:
            with transaction.atomic():
                book = get_object_or_404(PhysicalBook, id=book_id, isAvailable=True)
                book.isAvailable = False
                book.save()
                member.borrowed_books = book
                member.save()

            serializer = MemberSerializer(instance=member, context={'request': request})
            serializer.fields['memberId'].read_only = True
            serializer.fields['name'].read_only = True
            serializer.fields['borrowed_books'].queryset = PhysicalBook.objects.filter(isAvailable=True)

            return Response({'message': 'Physical book borrowed successfully.', 'member_info': serializer.data})
        except PhysicalBook.DoesNotExist:
            return Response({'error': 'Physical book not found.'}, status=status.HTTP_404_NOT_FOUND)