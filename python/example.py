from connect import get_mongo_client
from create import create_database, create_collection, insert_document
from read import get_one_match
from update import update_one_match
from delete import drop_collection, delete_one_match

# Mongo Instance URL
MONGO_INSTANCE_URL = "mongodb://localhost:27017"
# Flag to drop the collection after the script finishes
CLEAN_AFTER = True

client = get_mongo_client(MONGO_INSTANCE_URL)
if client != None:
    db_name = "testDB"
    collection_name = "testCollection"
    test_name = "TestDoc"
    document = {"Name": test_name}

    db = create_database(client, db_name)
    collection = create_collection(db, collection_name)
    new_document = insert_document(collection, document)

    db_list = client.list_database_names()
    collection_list = db.list_collection_names()

    # Ensure that the document is created properly and that both
    # the DB and the collection are now visible
    assert db_name in db_list and collection_name in collection_list, "Document creation failed"

    query_result = get_one_match(collection, document)

    # Ensure that the document can be fetched properly
    assert query_result != None, "Document fetching failed"

    new_name = "MoonDoc"
    new_data = {'$set': {"Name": new_name}}
    query = {"Name": {"$eq": document["Name"]}}

    update_result = update_one_match(collection, query, new_data)

    # Ensure that the document can be updated properly
    assert update_result.acknowledged == True, "Document update failed"

    delete_query = {"Name": {"$eq": new_name}}
    delete_result = delete_one_match(collection, delete_query)

    # Ensure that the document can be removed properly
    assert delete_result.acknowledged == True, "Document deletion failed"

    if collection != None and CLEAN_AFTER:
        drop_collection(collection)

    print("Script finalized properly")
else:
    print('Connection failed, ensure that the url provided is valid and that there is a mongo instance running')
