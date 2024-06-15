from flask import current_app as app
from bson import ObjectId

class DM:
    def __init__(self, sender_id, receiver_id, content, parent_mid=None):
        self.sender_id = sender_id
        self.receiver_id = receiver_id
        self.content = content
        self.parent_mid = parent_mid

    def save(self):
        dm_collection = app.mongo['dms']
        dm_collection.insert_one({
            "sender_id": self.sender_id,
            "receiver_id": self.receiver_id,
            "content": self.content,
            "parent_mid": self.parent_mid
        })

    @staticmethod
    def get_messages(user_id):
        dm_collection = app.mongo['dms']
        return list(dm_collection.find({"receiver_id": user_id}))

    @staticmethod
    def delete_message(mid):
        dm_collection = app.mongo['dms']
        dm_collection.delete_one({"_id": ObjectId(mid)})
