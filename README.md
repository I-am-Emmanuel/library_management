# library_management

Introduction 
This is a Django-based Library Management System that allows users to manage books, library members, and book borrowings. It provides a set of API endpoints for interacting with the system.

Features Book Management: 
You can create, retrieve, update, and delete books in the library. Each book has attributes like title, ISBN, publication date, and authors.

Member Management: 
You can create, retrieve, update, and delete library members. Members have attributes like member ID and name.

Book Borrowing: 
Members can borrow physical books from the library. The system ensures that borrowed books are marked as unavailable until they are returned.

Models 
Book Represents basic book information. Fields: title, ISBN, date_published, authors. Related to PhysicalBook and DigitalBook through foreign keys. 
PhysicalBook Represents physical copies of books. Fields: shelfLocation, isAvailable. Related to Book through a foreign key. Used in the Member model to represent books that members have borrowed. 
DigitalBook Represents digital copies of books. Fields: fileSize, download_link. Related to Book through a foreign key. 
Member Represents library members. Fields: memberId, name, borrowed_books (many-to-many relationship with PhysicalBook). Stores information about members, including books they have borrowed. 
Library Represents a library. Related to Book and Member models. 
Viewsets BookViewSet Provides CRUD operations for books. Includes a custom delete method to check if any members have borrowed the book before deletion.
MemberViewSet Provides CRUD operations for members. Includes a custom action borrow_physical_book to allow members to borrow physical books. This action also updates the availability of the book and associates it with the member. 
Usage 
Clone this repository to your local machine. Install the required dependencies by running pip install -r requirements.txt. Run the Django development server using python manage.py runserver. 
Access the API endpoints to manage books and members. 
API Endpoints 
api/books/: Endpoint for managing books. 
api/members/: Endpoint for managing members.
