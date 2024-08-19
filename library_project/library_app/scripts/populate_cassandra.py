from faker import Faker
import uuid
import time
from library_app.settings_cassandra import get_cassandra_session

def populate_cassandra():
    fake = Faker()
    db = get_cassandra_session()

    # Accéder à la collection dans Astra DB (l'équivalent d'une table dans Cassandra)
    transactions_collection = db.get_collection("transactions")

    for _ in range(100):
        transaction = {
            "transaction_id": str(uuid.uuid4()),
            "user_id": str(uuid.uuid4()),
            "book_title": fake.sentence(nb_words=4),
            "action": fake.random_element(elements=('borrow', 'return')),
            "timestamp": int(time.time())
        }

        # Insérer le document dans la collection
        transactions_collection.insert(transaction)

    print("Les transactions ont été insérées avec succès dans Astra DB.")

if __name__ == "__main__":
    populate_cassandra()
