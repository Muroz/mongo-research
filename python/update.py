def update_one_match(collection, query, new_data):
    """
    This function is for updating one document that
    matches the query provided
    Returns an instance of the UpdateResult class
    https://pymongo.readthedocs.io/en/stable/api/pymongo/results.html#pymongo.results.UpdateResult 
    """
    current_data = collection.find_one(query)
    update_result = collection.update_one(current_data, new_data)
    return update_result


def update_all_matches(collection, query, new_data):
    """
    This function is for updating all documents that
    match the query provided
    Returns an instance of the UpdateResult class
    https://pymongo.readthedocs.io/en/stable/api/pymongo/results.html#pymongo.results.UpdateResult 
    """
    collection.update_many(query, new_data)
