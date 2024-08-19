from django.conf import settings
from library_app.models import Book
from faker import Faker

def populate_mongodb():
    fake = Faker()

    for _ in range(100):
        book = Book(
            title=fake.sentence(nb_words=4),
            summary=fake.paragraph(),
            author=fake.name(),
            genre=fake.word(),
            published_year=fake.year()
        )
        book.save()

if __name__ == "__main__":
    populate_mongodb()
