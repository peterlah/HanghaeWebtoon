from flask import Flask, render_template, request, jsonify, session, redirect, url_for
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
def passwordCheck(pw_register_receive):
    pwd = pw_register_receive
    # 글자수 9 ~ 20, 영문 대소문자가 최소 한개씩 포함 필요
    # findall() 정규식과 매칭 되는 문자열을 리스트 형태로 반환
    if len(pwd) < 8 or len(pwd) > 21 and not \
        re.findall('[0-9]+', pwd) and not \
        re.findall('[a-z]', pwd) or not \
        re.findall('[A-Z]', pwd):
        return False
    # 비밀번호에는 최소 1개 이상의 특수 문자가 포함되어야 함
    elif not re.findall('[`~!@#$%^&*(),<.>/?]+', pwd):
        return False
    # 유효성 검사를 통과하면 True 값 반환
    return True

@app.route('/')
def home():
    return render_template('index.html')

# 메인 페이지
@app.route("/webtoon", methods=["GET", "POST"])
def webtoon_get():
    webtoon = list(db.webtoon_list.find())
    return jsonify({'result' : dumps(webtoon)})

# 상세 정보
@app.route("/detail/<string:id>", methods=["GET"])
def webtoon_detail(id):
    data = db.webtoon_list.find_one({"_id" : ObjectId(id)})
    return jsonify({"result" : dumps(data)})

# 검색
@app.route("/search", methods=["POST"])
def webtoon_search():
    search_keyword = request.form['search_title']
    webtoon = list(db.webtoon_list.find({'title' : { "$regex" : "^" + search_keyword}}))
    return jsonify({"result" : dumps(webtoon)})

# 회원가입
@app.route("/register", methods=["POST", "GET"])
def register_post():
    if request.method == 'POST':
        try:
            user_receive = request.form['registeruser']
            email_receive = request.form['registeremail']
            pw_receive = request.form['registerpassword']
            pw_check = request.form['re_password']
        
        except KeyError:    
            return jsonify({'msg': '양식을 모두 작성해주세요!', "status" : False})
        
        # 디비에서 해당 아이디의 사용자 정보를 조회
        user = db.user.find_one({'username': user_receive})

        # 패스워드 유효성 검사 True면 유효 False면 유효하지 않음
        pswd_logic = passwordCheck(pw_receive)

        # 패스워드 검사
        if pw_receive != pw_check:
            msg = "비밀번호가 일치하지 않습니다."
            return jsonify({'msg' : msg , 'status' : False})
        
        elif pswd_logic != True:
            msg = '비밀번호에는 최소 한개 이상의 특수문자, 영문 대소문자가 포함되어야 하며, 9~20자 사이여야 합니다.'
            return jsonify({'msg': msg, 'status' : False})
        
        elif user is not None: # 아이디 존재 여부 확인
            msg = '존재하는 아이디 입니다.'
            return jsonify({'msg': msg, 'status' : False})
        
        else:
            doc = {
                'username': user_receive,
                'mail': email_receive,
                'password': pw_receive
            }

            db.user.insert_one(doc)
            msg = '회원가입 완료!'
            
            return jsonify({'msg':msg, 'status' : True})
    
    else:
        return render_template('register.html')

# 로그인
@app.route("/login", methods=["POST", "GET"])
def login_post():
    if request.method == 'POST':
        try:
            user_receive = request.form['loginuser']
            pw_receive = request.form['loginpassword']

        except KeyError:
            return jsonify({'msg': '양식을 모두 작성해주세요!', 'status' : False})
        
        # 디비에서 해당 아이디의 사용자 정보를 조회
        user = db.user.find_one({'username': user_receive})

        # 아이디 존재 여부 확인
        if user is None:
            msg = "존재하지 않는 사용자입니다."
            return jsonify({'msg': msg, 'status' : False})
        
        # 비밀번호 일치 여부 확인
        if user['password'] != pw_receive:
            msg = "비밀번호가 일치하지 않습니다."
            return jsonify({'msg': msg, 'status' : False})
        
        else:
            # 세션 정보 등록
            session["username"] = user_receive
            msg = "login 성공!"           
            return jsonify({'msg': msg, 'status' : True})
    else:
        return render_template('login.html')

# 로그아웃    
@app.route('/logout', methods=["POST"])
def logout():
    # 세션 제거
    session.pop('username', None)
    msg = "로그아웃!"
    return jsonify({'msg' : msg, 'status': True })

# 마이페이지 Post
@app.route("/mypage", methods=["POST"])
def mypage_post():
    if 'username' in session:
        url_receive = request.form['url_give']
        comment_receive = request.form['comment_give']
        star_receive = request.form['star_give']
        
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
            'star': star_receive,
            'comment':comment_receive,
        }

        db.mywebtoon.insert_one(doc)
                
        # 데이터 검색 및 전용 value 값 넣어주기
        data = str(db.mywebtoon.find_one(doc)['_id'])
        db.mywebtoon.update_one(doc,{'$set':{'id':data}})

        return jsonify({'msg':'저장완료!'})
    
    else:
        return jsonify({'msg':'다시 로그인 해주세요.!'})

# 마이페이지 get
@app.route("/mypage", methods=["GET"])
def mypage_get():
    if 'username' in session:
        return render_template('mypage.html')
    else:
        return jsonify({'msg':'다시 로그인 해주세요.!'})

@app.route("/mypage/list", methods=["GET"])
def mypage_list_get():
    all_webtoon = list(db.mywebtoon.find({},{'_id':False}))
    return jsonify({'result': all_webtoon})

@app.route("/mypage/delete", methods=["POST"])
def movie_delete():
    id_receive = request.form['id_give']
    db.mywebtoon.delete_one({'id':id_receive})

    return jsonify({'msg':'삭제 완료!'})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5001, debug=True)