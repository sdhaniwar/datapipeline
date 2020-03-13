from flask import Flask, render_template
from flask import jsonify
from flask import request
from flask_pymongo import PyMongo
from pymongo import MongoClient
import json

app = Flask(__name__)

client = MongoClient("mongodb+srv://sdhaniwar:sumeet1508@cluster0-c00d8.gcp.mongodb.net/test?retryWrites=true&w=majority")
mydb = client['dataflow']
mycol = client['mycol']
db = client.dataflow

app.config['MONGO_DBNAME'] = 'dataflow'
app.config['MONGO_URI'] = 'mongodb+srv://sdhaniwar:sumeet1508@cluster0-c00d8.gcp.mongodb.net/test?retryWrites=true&w=majority'
serverstatus = db.command("serverStatus")
print(serverstatus)

mongo = PyMongo(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Fetch form data
        userDetails = request.form
        name = userDetails['name']
        email = userDetails['email']
        mydict = {'name': name , 'email': email}
        x = db.mycol.insert_one(mydict)

    return render_template("index.html")
@app.route('/result', methods= ['GET'])
def result():
  datas = db.mycol.find()
  resp = []
  for data in datas:
    data['_id'] = str(data['_id'])
    resp.append(data)
  return json.dumps(resp)  


if __name__ == '__main__':
    app.run(debug=True)