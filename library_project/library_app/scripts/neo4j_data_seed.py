from neo4j import GraphDatabase
from faker import Faker
import random

# Connexion à la base de données Neo4J
uri = "bolt://localhost:7687"
driver = GraphDatabase.driver(uri, auth=("neo4j", "fatee26ODC"))

fake = Faker()

def create_author_and_books(tx, author_name):
    # Créer un auteur
    tx.run("CREATE (a:Author {name: $name})", name=author_name)
    for _ in range(random.randint(1, 5)):  # Chaque auteur écrit entre 1 et 5 livres
        book_title = fake.sentence(nb_words=4)
        genre_name = fake.word()

        # Créer un genre
        tx.run("MERGE (g:Genre {name: $name})", name=genre_name)

        # Créer un livre
        tx.run("CREATE (b:Book {title: $title})", title=book_title)

        # Relation "WROTE" entre Auteur et Livre
        tx.run("""
            MATCH (a:Author {name: $author_name}), (b:Book {title: $book_title})
            CREATE (a)-[:WROTE]->(b)
        """, author_name=author_name, book_title=book_title)

        # Relation "BELONGS_TO" entre Livre et Genre
        tx.run("""
            MATCH (b:Book {title: $book_title}), (g:Genre {name: $genre_name})
            CREATE (b)-[:BELONGS_TO]->(g)
        """, book_title=book_title, genre_name=genre_name)

        # Ajout de lecteurs et recommandations
        for _ in range(random.randint(1, 7)):  # Chaque livre est lu par entre 1 et 7 lecteurs
            reader_name = fake.name()
            tx.run("MERGE (r:Reader {name: $name})", name=reader_name)

            # Relation "READ" entre Lecteur et Livre
            tx.run("""
                MATCH (r:Reader {name: $reader_name}), (b:Book {title: $book_title})
                CREATE (r)-[:READ]->(b)
            """, reader_name=reader_name, book_title=book_title)

            # Relation "RECOMMENDED" entre Lecteur et Livre
            if random.choice([True, False]):  # Certains lecteurs recommandent les livres
                tx.run("""
                    MATCH (r:Reader {name: $reader_name}), (b:Book {title: $book_title})
                    CREATE (r)-[:RECOMMENDED]->(b)
                """, reader_name=reader_name, book_title=book_title)

def populate_database():
    with driver.session() as session:
        for _ in range(10):  # Générer 10 auteurs avec leurs livres, genres, et lecteurs associés
            author_name = fake.name()
            session.write_transaction(create_author_and_books, author_name)

    driver.close()

if __name__ == "__main__":
    populate_database()
