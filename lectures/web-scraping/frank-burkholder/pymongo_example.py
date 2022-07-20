from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client['class_db']
table = db['teachers']

if __name__ == '__main__':
    example_record = {'name':'moses', 'age':31, 'friends':['ted', 'gahl']}
    table.insert_one(example_record)
    table.update_one({'name':'moses'}, {'$set':{'age':32}})
    table.find()
