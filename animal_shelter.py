from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, username, password):
        # Connection Variables
        # USER = 'aacuser'
        # PASS = 'Porkchop%3FC%40t%21July7'
        HOST = 'nv-desktop-services.apporto.com'
        PORT = 34995
        DB = 'AAC'
        COL = 'animals'

        # Initialize Connection
        self.client = MongoClient('mongodb://%s:%s@%s:%d/' % (username, password,HOST,PORT))
        self.database = self.client[DB]
        self.collection = self.database[COL]

    def create(self, data):
        """
        Insert a document into the collection.

        Args:
            data (dict): key-value pair that can be used with the MongoDB API insert call
        Returns:
            bool: True if the insert was successful, otherwise False
        """
        result = self.collection.insert_one(data)
        return result.acknowledged

    def read(self, query):
        """
        Search for documents matching the given query

        Args:
            query (dict): key-value lookup pair to be used with the MongoDB API find call
        Returns:
             list: a list of results. Will be empty if no match found
        """
        cursor = self.collection.find(query)
        return list(cursor)

    def update(self, query, new_values):
        """
        Updates any document that match the query with the values defined in new_values.

        Args:
             query (dict): A dictionary specifying the match condition.
            Any documents that match these conditions will be updated

            new_values (dict): A dictionary of the fields to update and the values to update them to.
            Passed inside MongoDB's $set operator to change or add fields.

        Returns:
             int: the number of documents modified.

        """
        result = self.collection.update_many(query, {"$set": new_values})
        return result.modified_count

    def delete(self, query):
        """
        Delete any document in the collection that matches the query.

        Args:
             query (dict): A dictionary specifying the match condition.
        Any documents that match these conditions will be deleted
        
        Returns:
             int: The number of documents deleted
        """
        result = self.collection.delete_many(query)
        return result.deleted_count
