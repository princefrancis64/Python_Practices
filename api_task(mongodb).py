# MondoDB
from flask import Flask , request,jsonify
import pymongo
from bson import ObjectId

app = Flask(__name__)

client = pymongo.MongoClient("mongodb+srv://princefrancis64:Oejb2e2l74Gz4NAK@cluster0.o5qm0dq.mongodb.net/?retryWrites=true&w=majority")
database = client['ineuron']
collection = database['api_task']


collection.update_one({"name": 'francis'}, {"$set": {"name": 'prince'}})
d = collection.find({'_id': ObjectId('64e5d400903bc15e1d681edb')})
for i in d:
    print(i)

@app.route("/insert/mongo",methods= ['POST'])
def insert():
    if request.method == 'POST':
        name = request.json['name']
        number = request.json['number']
        collection.insert_one({"name":name,"number":number})
        return jsonify(str("successfully inserted"))

@app.route("/update/mongo",methods = ['POST'])
def update():
    if request.method=='POST':
        name = request.json['name']
        collection.update_one({"name":name}, {"$set": {"name": "annies"}})
        return jsonify(str('successfully updated'))

@app.route("/update1/mongo",methods = ['POST'])
def update1():
    if request.method=='POST':
        name = request.json['name']
        collection.update_one({name:"real madrid"}, {"$set": {name: "barcelona is best"}})
        return jsonify(str('successfully updated'))

@app.route("/update2/mongo",methods = ['POST'])
def update2():
    if request.method=='POST':
        collection.update_one({'_id': ObjectId('64e5d400903bc15e1d681edb')}, {"$set": {'prince': "son"}})
        return jsonify('successfully updated')

@app.route("/fetchall/mongo",methods = ['POST'])
def fetchall():
    if request.method=='POST':
        l =[]
        d = collection.find()
        for i in d:
            l.append(i)
        return jsonify(str(l))

if __name__=='__main__':
    app.run()

