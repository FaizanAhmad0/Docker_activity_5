from flask import Flask, render_template, request, jsonify
from flask_pymongo import PyMongo

app = Flask(__name__, static_folder='../Frontend', template_folder='../Frontend')
app.config['MONGO_URI'] = 'mongodb://localhost:27017/userdb'
mongo = PyMongo(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    user_data = request.json
    name = user_data.get('name')
    email = user_data.get('email')
    if name and email:
        mongo.db.users.insert_one({'name': name, 'email': email})
        return jsonify({'message': 'Data inserted successfully'}), 200
    else:
        return jsonify({'message': 'Invalid data provided'}), 400

if __name__ == '__main__':
    app.run(debug=True)
