from pymongo import MongoClient
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# pyMongo
# URL 이스케이프 문자 : https://namu.wiki/w/URL%20escape%20code
client = MongoClient('mongodb+srv://swlah:%40zbqm1075711@cluster0.g93fmw7.mongodb.net/?retryWrites=true&w=majority')
db = client.webtoon

# index.html
@app.route('/', methods=["GET"])
def home():
    return render_template('index.html')

# 회원가입 페이지
@app.route("/register", methods=["POST"])
def register_post():
    user_register_receive = request.form.get('user')
    email_register_receive = request.form.get('email')
    pw_register_receive = request.form.get('password')
    pw_check_receive = request.form.get('re_password')

    if pw_register_receive != pw_check_receive:
        return jsonify({'msg': '비밀번호가 일치하지 않습니다.'})

    doc = {
        'username': user_register_receive,
        'mail': email_register_receive,
        'password': pw_register_receive
    }

    db.user.insert_one(doc)

    return jsonify({'msg':'회원가입 완료!'})


@app.route("/register", methods=["GET"])
def register_get():
    return render_template('register.html')

# 로그인 페이지
@app.route("/login", methods=["POST"])
def login_post():
    user_receive = request.form.get('user_give')
    pw_receive = request.form.get('pw_give')
    
    # 디비에서 해당 아이디의 사용자 정보를 조회
    user = db.user.find_one({'username': user_receive})
    
    # 아이디 존재 여부 확인
    if user is None:
        return jsonify({'msg': '존재하지 않는 사용자입니다.'})
    
    # 비밀번호 일치 여부 확인
    if user.get('password') != pw_receive:
        return jsonify({'msg': '비밀번호가 일치하지 않습니다.'})
    else:
    	return jsonify({'msg': 'login 성공!'})

@app.route("/login", methods=["GET"])
def login_get():
    return render_template('login.html')

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
