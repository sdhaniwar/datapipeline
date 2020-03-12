from flask import Flask, render_template
from flask import jsonify
from flask import request
from flask_pymongo import PyMongo

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'dataflow'
app.config['MONGO_COLLECTIONNAME'] = 'userdata'
app.config['MONGO_URI'] = 'mongodb+srv://sdhaniwar:<sumeet1508>@cluster0-c00d8.gcp.mongodb.net/test?retryWrites=true&w=majority'

mongo = PyMongo(app)

@app.route('/')
def home():
    return 'This is the homepage'

@app.route('/addata', methods=['POST'])
def adddata():
  dataflow = mongo.db.dataflow.userdata
  name = request.json['name']
  distance = request.json['distance']
  dataflow_id = dataflow.insert({'name': name, 'distance': distance})
  return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)