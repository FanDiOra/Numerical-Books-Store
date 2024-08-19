from astrapy import DataAPIClient

# Remplacez 'YOUR_TOKEN' par votre jeton d'application généré dans Astra DB
CLIENT_TOKEN = "AstraCS:QtgkNwaTMlPCmmBGoBawxdsb:dfc6b83a899f0c0f122c3e4e26670d6e542469dee2177ca168b7a9a5d5a00b3e"

# Remplacez par l'endpoint API et le namespace de votre keyspace
ASTRA_DB_URL = "https://3bf74ae0-52ae-4387-bab8-fc4b19e8b957-us-east-2.apps.astra.datastax.com"
ASTRA_DB_NAMESPACE = "books_keyspace"

def get_cassandra_session():
    # Initialise le client DataAPI pour Astra DB
    client = DataAPIClient(CLIENT_TOKEN)
    
    # Connexion à la base de données Astra
    db = client.get_database_by_api_endpoint(
        ASTRA_DB_URL,
        namespace=ASTRA_DB_NAMESPACE
    )
    
    print(f"Connecté à Astra DB : {db.list_collection_names()}")
    return db
