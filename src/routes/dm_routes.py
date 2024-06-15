from flask import Blueprint, request, jsonify, session, render_template
from src.models.dm import DM
from src.models.user import User

dm_bp = Blueprint('dm_bp', __name__)

@dm_bp.route('/send', methods=['POST'])
def send_message():
    if 'userid' not in session:
        return jsonify({"message": "Unauthorized"}), 401

    data = request.get_json()
    sender_id = session['userid']
    receiver_id = data['receiver_id']
    content = data['content']
    parent_mid = data.get('parent_mid')
    dm = DM(sender_id, receiver_id, content, parent_mid)
    dm.save()
    print(data)
    return jsonify({"message": "메시지 송신"}), 201

@dm_bp.route('/list', methods=['GET'])
def get_messages():
    if 'userid' not in session:
        return jsonify({"message": "권한 없음"}), 401

    user_id = session['userid']
    messages = DM.get_messages(user_id)
    return jsonify(messages), 200

@dm_bp.route('/delete/<mid>', methods=['DELETE'])
def delete_message(mid):
    if 'userid' not in session:
        return jsonify({"message": "권한 없음"}), 401

    DM.delete_message(mid)
    return jsonify({"message": "메시지 삭제 성공"}), 200


@dm_bp.route('/send', methods=['POST'])
def send_dm():
    if 'userid' not in session:
        return jsonify({"message": "권한 없음"}), 401

    data = request.get_json()
    print(data)
    print(session)
    sender_id = session['userid']
    receiver_id = data['receiver_id']
    content = data['content']
    parent_mid = data.get('parent_mid')
    dm = DM(sender_id, receiver_id, content, parent_mid)
    dm.save()
    return jsonify({"message": "메시지 송신"}), 201

@dm_bp.route('/delete_message/<mid>', methods=['DELETE'])
def delete_message_by_mid(mid):
    if 'userid' not in session:
        return jsonify({"message": "권한 없음"}), 401

    DM.delete_message(mid)
    return jsonify({"message": "메시지 삭제 성공"}), 200

@dm_bp.route('/sendingDM', methods=['GET'])
def sendingDM_page():
    return render_template('sending-d-m.html')

@dm_bp.route('/sendedDM', methods=['GET'])
def sendedDM_page():
    return render_template('sended-d-m.html')

@dm_bp.route('/receivedDM', methods=['GET'])
def receivedDM_page():
    # receiver_id가 현재 로그인한 사용자의 id인 메시지들을 가져옴
    if 'userid' not in session:
        return jsonify({"message": "권한 없음"}), 401
    
    user_id = session['userid']
    messages = DM.get_messages(user_id)

    for message in messages:
        message['sender_name'] = User.get_user_name(message['sender_id'])

    return render_template('recieved-d-m.html', messages=messages)