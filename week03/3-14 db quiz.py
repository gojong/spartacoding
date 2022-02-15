from select import select
from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta


# title2 = db.movies.find_one({'title':'매트릭스'})
# # print(title2['star']) # 1개 평점 찾기

# target_star = title2['star']

# target_movies = list(db.movies.find({'star':target_star},{'_id':False}))

# for target in target_movies:
#     print(target['title'])
    
#------------

db.movies.update_one({'title':'매트릭스'},{'$set':{'star':'0'}}) # 평점 0으로 바꾸기 (기존 6.33)

