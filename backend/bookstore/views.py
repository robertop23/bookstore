from bookstore.models import Book, Consumer
from bookstore.serializers import BookSerializer, ConsumerBookSerializer
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated


class BookViewSet(viewsets.ReadOnlyModelViewSet):
    """
    A simple ListAPIView for listing or retrieving Books.
    """

    # permission_classes = (IsAuthenticated,)

    serializer_class = BookSerializer

    def get_queryset(self):
        if 'store' in self.kwargs:
            return Book.objects.filter(store=self.kwargs['store'])
        else:
            return Book.objects.all()


class BookPurchaseView(APIView):
    """
    Purchase a Book, +1 to the book views and check form +1M rule to
    give 0,05 to the book owner
    """

    permission_classes = (IsAuthenticated,)

    def post(self, request, book=None):
        serializer = ConsumerBookSerializer(data=request.data)
        if serializer.is_valid():
            consumer = Consumer.objects.get(consumer=request.user.id)
            serializer.save(consumer=consumer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
