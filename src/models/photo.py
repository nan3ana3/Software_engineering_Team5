from flask import current_app as app
import os
from werkzeug.utils import secure_filename
from datetime import datetime
from bson import ObjectId

class Photo:
    def __init__(self, uploader_id, description, imageName):
        self.uploader_id = uploader_id
        self.description = description
        self.imageName = imageName


    def save(self, image_file, keywords):
        # 폴더에 이미지 저장
        upload_folder = os.path.join(app.config['UPLOAD_FOLDER'])
        if not os.path.exists(upload_folder):
            os.makedirs(upload_folder)
        
        current_time = datetime.now().strftime("%Y%m%d%H%M%S")
        filename = current_time + "." + secure_filename(image_file.filename)
        image_path = os.path.join(upload_folder, filename)
        image_file.save(image_path)

        # db에는  이미지 파일명 저장
        photo_collection = app.mongo['photos']
        photo_collection.insert_one({
            "uploader_id": self.uploader_id,
            "description": self.description,
            "imageName": filename,
            "keywords": keywords
        })

        return filename

    
    @staticmethod
    def search_by_keyword(keyword):
        photo_collection = app.mongo['photos']
        return list(photo_collection.find({"keywords": {"$regex": keyword, "$options": "i"}}))
    
    @staticmethod
    def get_all_photos():
        photo_collection = app.mongo['photos']
        return list(photo_collection.find({}))
    

    @staticmethod
    def get_photos_by_user(user_id):
        photo_collection = app.mongo['photos']
        return list(photo_collection.find({"uploader_id": user_id}))
    
    @staticmethod
    def get_photos_by_photoId(photo_id):
        photo_collection = app.mongo['photos']
        photo = photo_collection.find({'_id': ObjectId(photo_id)})
        return list(photo) 