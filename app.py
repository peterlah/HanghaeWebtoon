from flask import Flask, render_template, request, jsonify, session
from pymongo import MongoClient
from bson.json_util import dumps
from bson.objectid import ObjectId
from bs4 import BeautifulSoup
import re
import requests

app = Flask(__name__)
client = MongoClient('mongodb+srv://chunws:test@chunws.w8zkw9b.mongodb.net/?retryWrites=true&w=majority')
db = client.chunws

# 세션을 위한 secret 키 생성
app.secret_key = "hanghaewebtooner"

# 비밀번호 유효성 검사 함수
def passwordCheck(pwd):
    # 글자수 9 ~ 20, 영문 대소문자가 최소 한개씩 포함 필요
    # findall() 정규식과 매칭 되는 문자열을 리스트 형태로 반환
    if len(pwd) < 8 or len(pwd) > 21 and not \
        re.findall('[0-9]+', pwd) and not \
        re.findall('[a-z]', pwd) or not re.findall('[A-Z]', pwd):
        return False
    # 비밀번호에는 최소 1개 이상의 특수 문자가 포함되어야 함
    elif not re.findall('[`~!@#$%^&*(),<.>/?]+', pwd):
        return False
    # 유효성 검사를 통과하면 True 값 반환
    return True

@app.route('/')
def home():
    return render_template('index.html')

##### 우상님 작성 내용 #####
@app.route("/webtoon", methods=["GET"])
def webtoon_get():
    all_webtoon = list(db.webtoon_list.find())
    return jsonify({'result' : dumps(all_webtoon)})

@app.route("/detail/<string:id>", methods=["GET"])
def webtoon_detail(id):
    data = db.webtoon_list.find_one({"_id" : ObjectId(id)})
    return jsonify({"result" : dumps(data)})

##### 상우님 작성 내용 #####
# 회원가입 페이지
@app.route("/register", methods=["POST"])
def register_post():
    user_register_receive = request.form.get('user')
    email_register_receive = request.form.get('email')
    pw_register_receive = request.form.get('password')
    pw_check_receive = request.form.get('re_password')

    # 디비에서 해당 아이디의 사용자 정보를 조회
    user = db.user.find_one({'username': user_register_receive})

    # 패스워드 유효성 검사 True면 유효 False면 유효하지 않음
    pswd_logic = passwordCheck(pw_register_receive)

    # 패스워드 검사
    if pw_register_receive != pw_check_receive:
        return jsonify({'msg': '비밀번호가 일치하지 않습니다.'})
    elif pswd_logic != True:
        return jsonify({'msg': '비밀번호에는 최소 한개 이상의 특수문자, 영문 대소문자가 포함되어야 하며, 9~20자 사이여야 합니다.'})
    elif user is not None: # 아이디 존재 여부 확인
        return jsonify({'msg': '존재하는 아이디 입니다.'})
    else:
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
        # 세션 정보 등록
        session["username"] = user_receive
        session["password"] = pw_receive
        session["id"] = str(user.get("_id"))
        
        # 세션 유지 시간 설정
        session.permanent = True
        
        return jsonify({'msg': 'login 성공!'})

@app.route("/login", methods=["GET"])
def login_get():
    return render_template('login.html')
    
##### 보슬님 작성 내용 #####
# /webtoon -> /mypage로 수정, 함수명 변경
@app.route("/mypage", methods=["POST"])
def mypage_post():
    url_receive = request.form['url_give']
    comment_receive = request.form['comment_give']
    
    headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    data = requests.get(url_receive,headers=headers)

    soup = BeautifulSoup(data.text, 'html.parser')

    ogtitle = soup.select_one('meta[property="og:title"]')['content']
    ogdesc = soup.select_one('meta[property="og:description"]')['content']
    ogimage = soup.select_one('meta[property="og:image"]')['content']
  
    doc = {
        'title':ogtitle,
        'desc':ogdesc,
        'image':ogimage,
        'comment':comment_receive,
    }
    # collection 명 수정(webtoon->mywebtoon)
    db.mywebtoon.insert_one(doc)
            
    return jsonify({'msg':'POST 등록완료!'})

# /webtoon -> /mypage로 수정, 함수명 
@app.route("/mypage", methods=["GET"])
def mypage_get():
    return jsonify({'msg':'GET 연결 완료!'})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5001, debug=True)