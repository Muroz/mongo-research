
def create_database(client, db_name):
    """
    This function is for creating a database
    within the client provided. This db won't appear within
    the client until it has documents within it
    Returns an instance of the Database class
    https://pymongo.readthedocs.io/en/stable/api/pymongo/database.html?highlight=database#pymongo.database.Database
    """
    db = client[db_name]
    return db


def create_collection(db, name):
    """
    This function is for creating a collection
    within the database provided. This collection won't appear within
    the db until it has documents within it
    Returns an instance of the Collection class
    https://pymongo.readthedocs.io/en/stable/api/pymongo/collection.html?highlight=collection#pymongo.collection.Collection
    """
    collection = db[name]
    return collection


def insert_document(collection, document):
    """
    This function is for creating a document 
    within the collection provided
    Returns an instance of the InsertOneResult class
    https://pymongo.readthedocs.io/en/stable/api/pymongo/results.html#pymongo.results.InsertOneResult
    """
    new_item = collection.insert_one(document)
    return new_item


def insert_many_documents(collection, documents):
    """
    This function is for creating multiple documents 
    within the collection provided
    Returns an instance of the InsertManyResult class
    https://pymongo.readthedocs.io/en/stable/api/pymongo/results.html#pymongo.results.InsertManyResult
    """
    new_items = collection.insert_many(documents)
    return new_items
