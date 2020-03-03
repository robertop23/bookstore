from django.contrib import admin
from bookstore.models import (
    Store,
    Publisher,
    Author,
    Consumer,
    Category,
    Book,
    ConsumerBook,
    Earning,
)

admin.site.register(Store)
admin.site.register(Publisher)
admin.site.register(Author)
admin.site.register(Consumer)
admin.site.register(Category)
admin.site.register(Book)
admin.site.register(ConsumerBook)
admin.site.register(Earning)
