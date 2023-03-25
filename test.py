from pymongo import MongoClient
client = MongoClient('mongodb+srv://chunws:test@chunws.w8zkw9b.mongodb.net/?retryWrites=true&w=majority')
db = client.chunws

all_list = list(db.webtoon_list.find({},{'_id':False}))
# print(all_list[0])         # 0번째 결과값을 보기
# print(all_list[0]['name']) # 0번째 결과값의 'name'을 보기
client = MongoClient('mongodb+srv://swlah:zbqm0621@cluster0.g93fmw7.mongodb.net/?retryWrites=true&w=majority')
db2 = client.webtoon
for a in all_list:      # 반복문을 돌며 모든 결과값을 보기
    db2.webtoon_list.insert_one(a)