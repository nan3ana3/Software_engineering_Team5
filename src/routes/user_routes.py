<<<<<<< Updated upstream
from flask import Blueprint, request, jsonify, session, render_template, redirect
=======
from flask import Blueprint, request, jsonify, session, render_template, redirect, url_for
>>>>>>> Stashed changes
from src.models.user import User
from src.models.photo import Photo

user_bp = Blueprint('user_bp', __name__)


@user_bp.route('/signup', methods=['POST'])
def sign_up():
    data = request.get_json()
    username = data['username']
    userid = data['userid']
    password = data['password']
    confirmPassword = data['confirmPassword']
    if password != confirmPassword:
        return jsonify({"message": "비밀번호가 일치하지 않습니다"}), 400
    existing_user = User.find_by_userid(userid)
    if existing_user:
        return jsonify({"message": "이미 존재하는 유저입니다"}), 400

    user = User(username, userid, password)
    user.save()
    return jsonify({"message": "유저 생성"}), 201

@user_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    userid = data['userid']
    password = data['password']
    user = User.login(userid, password)
    if user:
        session['userid'] = userid
        return jsonify({"message": "로그인 성공"}), 200
    return jsonify({"message": "로그인 실패"}), 401

@user_bp.route('/signout', methods=['POST'])
def sign_out():
    session.pop('userid', None)
    return jsonify({"message": "로그아웃 성공"}), 200


#2,3번 조건
@user_bp.route('/list', methods=['GET'])
def get_user_list():
    if 'userid' not in session:
        users = User.get_user_list()
        return render_template('index.html', users=users)
    else:
        users, photos = User.get_user_listAndPhoto()
<<<<<<< Updated upstream
=======
        print(photos)
>>>>>>> Stashed changes
        return render_template('main-loged-in.html', users=users, photos=photos)




@user_bp.route('/mypage', methods=['GET'])
def mypage_page():
    if 'userid' not in session:
<<<<<<< Updated upstream
        return redirect('/login')
=======
        return redirect(url_for('user_bp.login'))
>>>>>>> Stashed changes
    current_userid = session['userid']
    current_username = User.find_by_userid(current_userid)['username']

    # 현재 사용자가 올린 모든 이미지 가져오기
    photos = Photo.get_photos_by_user(current_userid)
    
    return render_template('my-page.html', username=current_username, photos=photos)


@user_bp.route('/login', methods=['GET'])
def login_page():
    return render_template('login.html')


@user_bp.route('/signup', methods=['GET'])
def signup_page():
    return render_template('signup.html')



@user_bp.route('/modifyme', methods=['GET'])
def modifyme_page():
    return render_template('modify-me.html')