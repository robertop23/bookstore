from django.urls import path
from bookstore.views import BookViewSet, BookPurchaseView

urlpatterns = [
    # Books
    # http://127.0.0.1:8000/books/1/5
    path('<int:store>/<int:pk>', BookViewSet.as_view({'get': 'retrieve'})),
    # http://127.0.0.1:8000/books/1
    path('<int:store>', BookViewSet.as_view({'get': 'list'})),
    # {"consumer":1,"book":5,"status":"purchased"}
    path('bookpurchase', BookPurchaseView.as_view()),
]
