def get_one_match(collection, query):
    """
    This function is for looking for one document
    that matches the query provided
    Returns a matching document or None
    """
    item = collection.find_one(query)
    return item


def get_all_matches(collection, query):
    """
    This function is for looking for all documents
    that match the query provided
    Returns an instance of the Cursor class 
    https://pymongo.readthedocs.io/en/stable/api/pymongo/cursor.html#pymongo.cursor.Cursor
    """
    items = collection.find(query)
    return items


def get_collection_items(collection):
    """
    This function is for looking for all documents
    within a collection
    Returns an instance of the Cursor class 
    https://pymongo.readthedocs.io/en/stable/api/pymongo/cursor.html#pymongo.cursor.Cursor
    """
    items = collection.find({})
    return items
