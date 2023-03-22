from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

from pymongo import MongoClient
from bson.json_util import dumps
from bson.objectid import ObjectId
clinet = MongoClient('mongodb+srv://chunws:test@chunws.w8zkw9b.mongodb.net/?retryWrites=true&w=majority')
db = clinet.chunws

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/webtoon", methods=["GET"])
def webtoon_get():
    all_webtoon = list(db.webtoon_list.find())
    return jsonify({'result' : dumps(all_webtoon)})

@app.route("/detail/<string:id>", methods=["GET"])
def webtoon_detail(id):
    data = db.webtoon_list.find_one({"_id" : ObjectId(id)})
    return jsonify({"result" : dumps(data)})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5001, debug=True)