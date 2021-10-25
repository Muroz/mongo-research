import pymongo
from pymongo.errors import ConnectionFailure


def get_mongo_client(url):
    """
    This function connects to a mongodb
    based on the provided URL 
    Returns an instance of the MongoClient class if available
    https://pymongo.readthedocs.io/en/stable/api/pymongo/index.html?highlight=MongoClient#pymongo.MongoClient
    """
    client = pymongo.MongoClient(url)
    try:
        client.admin.command('ping')
        return client
    except ConnectionFailure:
        print("Server not available")
        return None
