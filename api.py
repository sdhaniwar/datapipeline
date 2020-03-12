from flask import Flask
from flask import jsonify
from flask import request, PyMongo

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'dataflow'
app.config['MONGO_URI'] = 'mongodb+srv://sdhaniwar:<sumeet1508>@cluster0-c00d8.gcp.mongodb.net/test?retryWrites=true&w=majority'

mongo = PyMongo(app)


@app.route('/dataflow', methods=['POST'])
def add_data():
  dataflow = mongo.db.dataflow
  name = request.json['name']
  distance = request.json['distance']
  dataflow_id = dataflow.insert({'name': name, 'distance': distance})
  new_star = dataflow.find_one({'_id': dataflow_id })
  output = {'name' : new_star['name'], 'distance' : new_star['distance']}
  return jsonify({'result' : output})

if __name__ == '__main__':
    app.run(debug=True)