from flask import Flask, jsonify,render_template,request,redirect


app = Flask(__name__)

# Configure db
db = yaml.load(open('db.yaml'))
app.config['MYSQL_HOST'] = db['mysql_host']
app.config['MYSQL_USER'] = db['mysql_user']
app.config['MYSQL_PASSWORD'] = db['mysql_password']
app.config['MYSQL_DB'] = db['mysql_db']

mysql = MySQL(app)
@app.route('/todo/api', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Fetch form data
        userDetails = request.form
        id = userDetails['id']
        emp_id=userDetails['emp_id']
        name=userDetails['name']
        industry=userDetails['industry']
        mobile=userDetails['mobile']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO users(id,emp_id,name,industry,mobile) VALUES(%s, %s,%s,%,s,%s)",(id,emp_id,name,industry,mobile))
        mysql.connection.commit()
        cur.close()
        return redirect('/users')
    return render_template('index.html')

@app.route('/')
def home():
     return "We are at the home page"

if __name__ == '__main__':
    app.run(debug=True)