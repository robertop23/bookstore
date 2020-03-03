from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, timedelta


class Store(models.Model):
    name = models.CharField(max_length=50)
    country = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Publisher(models.Model):
    publisher = models.OneToOneField(User, on_delete=models.CASCADE)
    logo = models.ImageField(upload_to='img/logo', blank=True, null=True)
    country = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.publisher.first_name} {self.publisher.last_name}'


class Author(models.Model):
    author = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='img/avatar', blank=True, null=True)
    country = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.author.first_name} {self.author.last_name}'


class Consumer(models.Model):
    consumer = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='img/avatar', blank=True, null=True)
    country = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.consumer.first_name} {self.consumer.last_name}'


class Earning(models.Model):
    # the author/publisher
    author = models.OneToOneField(
        Author, blank=True, null=True, on_delete=models.CASCADE
    )
    publisher = models.OneToOneField(
        Publisher, blank=True, null=True, on_delete=models.CASCADE
    )
    # total earned amount author/published
    earnings = models.FloatField(blank=True, null=True, default=0.0)
    # withdrawed amount
    withdrawed = models.FloatField(blank=True, null=True, default=0.0)

    def __str__(self):
        if self.author:
            return f'{self.author.author.first_name} {self.author.author.last_name}  \
                  - {self.earnings}'
        else:
            return f'{self.publisher.publisher.first_name} {self.publisher.publisher.last_name}  \
                  - {self.earnings}'


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"


class Book(models.Model):
    title = models.CharField(max_length=200)
    publish_date = models.DateField()
    summary = models.TextField()
    cover = models.ImageField(
        upload_to='bookstore/covers',
        default='bookstore/covers/empty_book.png',
        blank=True,
        null=True,
    )
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, blank=True, null=True, on_delete=models.CASCADE)
    publisher = models.ForeignKey(
        Publisher, blank=True, null=True, on_delete=models.CASCADE
    )
    store = models.ForeignKey(Store, blank=True, null=True, on_delete=models.CASCADE)
    book_content = models.FileField(upload_to='book_files/', blank=True, null=True)

    def __str__(self):
        return self.title


STATUS = [
    ("purchased", "Purchased"),
    ("rented", "Rented"),
]


class ConsumerBook(models.Model):
    consumer = models.ForeignKey(Consumer, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    status = models.CharField(max_length=30, choices=STATUS)
    # If rented, then this will be the due date
    due_date = models.DateField(blank=True, null=True)

    def save(self, *args, **kwargs):
        # if first time creating transaction (as opposed to on update)
        if not self.id:
            print(self.status)
            if self.status == 'rented':
                self.due_date = datetime.now() + timedelta(days=30)
            # check for +1 to increase Earnings
            books = ConsumerBook.objects.filter(book=self.book)
            # CHANGE THIS TO 1000000 in production
            if len(books) >= 5:
                # then give author/publisher 0,05
                author = self.book.author
                publisher = self.book.publisher
                earning = {}
                if author:
                    try:
                        earning = Earning.objects.get(author=author)
                    except Earning.DoesNotExist:
                        earning = {'author': author, 'earnings': 0.05}
                        Earning.objects.create(**earning)
                    else:
                        earning.earnings += 0.05
                        earning.save()
                if publisher:
                    try:
                        earning = Earning.objects.get(publisher=publisher)
                    except Earning.DoesNotExist:
                        earning = {'publisher': publisher, 'earnings': 0.05}
                        Earning.objects.create(**earning)
                    else:
                        earning.earnings += 0.05
                        earning.save()

        # call and return default save method after custom rule
        return super(ConsumerBook, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.consumer.consumer.first_name} {self.consumer.consumer.last_name} - {self.book.title}'
