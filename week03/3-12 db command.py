#pymongo로 db조작하기

from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta

# 코딩 시작

# insert / find / update / delete 명령어

#------------------------------------

# doc = {'name':'하하','age':27}
# db.users.insert_one(doc)


#---------------------------
#same_ages = list(db.users.find({},{'_id':False})) #전체 db 가져올때 빈칸으로 한다
# same_ages = list(db.users.find({'age':21},{'_id':False}))
# print(same_ages)

#---------------------------


# user = db.users.find_one({'name':'bobby'},{'_id':False})

#-------------------------

# db.users.update_one({'name':'bobby'},{'$set':{'age':19}}) #하나 네임 바비만 교체한다

# db.users.update_many({'name':'bobby'},{'$set':{'age':19}}) #전체적으로 변경한다

#-----------------------------

#db.users.delete_one({'name':'bobby'})

#--------------------------------

# 저장 - 예시
doc = {'name':'bobby','age':21}
db.users.insert_one(doc)

# 한 개 찾기 - 예시
user = db.users.find_one({'name':'bobby'})

# 여러개 찾기 - 예시 ( _id 값은 제외하고 출력)
same_ages = list(db.users.find({'age':21},{'_id':False}))

# 바꾸기 - 예시
db.users.update_one({'name':'bobby'},{'$set':{'age':19}})

# 지우기 - 예시
db.users.delete_one({'name':'bobby'})