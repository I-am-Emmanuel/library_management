from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet, MemberViewSet

router = DefaultRouter()
router.register(r'books', BookViewSet)
router.register(r'members', MemberViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/members/<int:pk>/borrow_physical_book/', MemberViewSet.as_view({'post': 'borrow_physical_book'}), name='borrow-physical-book'),
]