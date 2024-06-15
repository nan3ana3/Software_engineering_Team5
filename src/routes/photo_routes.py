from flask import Blueprint, request, jsonify, session, render_template, request, redirect
from src.models.photo import Photo

photo_bp = Blueprint('photo_bp', __name__)

@photo_bp.route('/upload', methods=['POST'])
def upload_photo():
    if 'userid' not in session:
        return jsonify({"message": "인증 실패"}), 401
    image = request.files['image']
    description = request.form['description']
    user_id = session['userid']
    keywords = request.form.get('keywords', '').split(',')

    # Photo 인스턴스를 생성해 이미지를 저장
    photo = Photo(user_id, description, image.filename)
    saved_filename = photo.save(image, keywords)

    return jsonify({"message": "사진 업로드 성공", "filename": saved_filename}), 201

@photo_bp.route('/search', methods=['GET'])
def search_photos_by_keyword():
    keyword = request.args.get('keyword', '')

    photos = Photo.search_by_keyword(keyword)
    print(photos)
    
    return render_template('main-loged-in.html', photos=photos)





@photo_bp.route('/uploadpost', methods=['GET'])
def uploadpost_page():
    if 'userid' not in session:
        return jsonify({"message": "인증 실패"}), 401
    return render_template('upload-post.html')


@photo_bp.route('/otherpost', methods=['GET'])
def otherpost():
    return render_template('otherpost.html')

@photo_bp.route('/mypost', methods=['GET'])
def mypost():
    photo_id = request.args.get('id')
    photo = Photo.get_photos_by_photoId(photo_id)
    print(photo)
    return render_template('my-post.html', photo=photo)