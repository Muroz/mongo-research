def delete_one_match(collection, query):
    """
    This function is for deleting one document
    that matches the query provided
    Returns an instance of the DeleteResult class
    https://pymongo.readthedocs.io/en/stable/api/pymongo/results.html#pymongo.results.DeleteResult    
    """
    delete_result = collection.delete_one(query)
    return delete_result


def delete_all_matches(collection, query):
    """
    This function is for deleting all documents
    that match the query provided
    Returns an instance of the DeleteResult class
    https://pymongo.readthedocs.io/en/stable/api/pymongo/results.html#pymongo.results.DeleteResult    
    """
    delete_result = collection.delete_many(query)
    return delete_result


def drop_collection(collection):
    """
    This function is for removing a collection and
    all of the documents within it
    Void function
    """
    collection.drop()
