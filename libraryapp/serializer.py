from rest_framework import serializers

from .models import Book, Member, PhysicalBook

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'authors', 'isbn']

class PhysicalBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhysicalBook
        fields = ['book']

class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = ['memberId', 'name', 'borrowed_books']

    def create(self, validated_data):
        # Extract the borrowed_books data from validated_data
        borrowed_books_data = validated_data.pop('borrowed_books')

        # Create a new Member instance without borrowed_books
        member = Member.objects.create(**validated_data)

        # Create a new PhysicalBook instance using borrowed_books_data
        physical_book = PhysicalBook.objects.create(**borrowed_books_data)

        # Associate the PhysicalBook with the Member
        member.borrowed_books = physical_book
        member.save()

        return member



# class MemberSerializer(serializers.ModelSerializer):
#     borrowed_book = PhysicalBookSerializer(source='borrowed_books')  # Use PhysicalBookSerializer

#     class Meta:
#         model = Member
#         fields = ['memberId', 'name', 'borrowed_book']