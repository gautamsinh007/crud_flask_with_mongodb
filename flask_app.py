# https://www.youtube.com/watch?v=kZlet-OepxE  for mongodb in flask

from flask  import  Flask , request, redirect, url_for
from flask_pymongo import pymongo
import certifi
import json
from flask.json import jsonify

from bson.json_util import dumps
from bson.objectid import ObjectId

app = Flask(__name__)

try:
    
    myclient = pymongo.MongoClient("mongodb+srv://gautamsinh:gau123123@cluster0.2c9i6px.mongodb.net/test",  tlsCAFile=certifi.where())

    iisd_db = myclient["test"]

    sample_e = iisd_db["e"] 
    # print(sample_e)
except Exception as e:
    print("Exception in Connecting the data",e)
    
    


# @app.route('/users', methods = ['POST'])
# def create_user():
#     try:
#         user ={"name":"gautam","lastname":"makwana"}
#         dbresponce = sample_e.users.insert_one(user)
        
#         for attr in dir(dbresponce):
#             print(attr)
            
#     except Exception as e:  
#         print(e)
        
@app.route('/home', methods=['GET', 'POST'])
def index():
    data = request.get_json()
    if request.method=='POST':
        content = data['content']
        degree = data['degree']
        sample_e.insert_one({'content': content, 'degree': degree})
        
        print(content,"????????")
        print(degree,">>>>>>>>>>")
        print(sample_e,"---------------------------------------")
        return  "data added"


@app.route("/data")
def demo():
    result = sample_e.find()
    res = []
    for  i in result:
        del i["_id"]
        res.append(i)

    print(res)

    return  jsonify({"msg":res})
 
#  find_many
 
@app.route("/one/<string:content>")
def demo1(content):
    result = sample_e.find_one({"content":content})
    # result = sample_e.find_many({"content":content})
    # print(result,"=================")
    del (result['_id'])
    
    
    return jsonify(result)
    
 
# delete_many   
    
@app.route("/delete/<string:content>", methods = ["DELETE"])
def delete(content):
    # result = sample_e.delete_one({"content":content})
    sample_e.delete_many({"content":content})
    # del result
    # del (result['_id'])
    
    
    return "data delete"


# update
@app.route("/update/<string:content>", methods=['PUT', "GET"])
def update(content):
    data = request.get_json()
    # if request.method == "POST":
        
        
        # result = sample_e.delete_one({"content":content})
    # result = sample_e.find_one({"content":content})
    
    abc = request.json['content']
    bca =   request.json['degree']
    print(content)
    # print(degree)
    
    
    sample_e.update_one({"content":content},{"$set":{"content":abc, "degree":bca}})
    
    return "data updated"







  
  
        
if __name__ =='__main__':  
    app.run(debug = True)  


# /Applications/Python\ 3.0.9/Install\ Certificates.command