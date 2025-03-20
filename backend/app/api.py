from flask import Flask, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient('mongodb', 27017)
db = client['test-database']
collection = db['test-collection']

@app.route('/')
def hello_world():
    return '<h1>Hello, World!</h1>'

# Endpoint for adding the user
@app.route('/users', methods=['POST'])
def add_user():
    user_data = request.json
    if not user_data or not user_data.get('name') or not user_data.get('email'):
        return jsonify({"error": "Invalid data. 'name' and 'email' are required."}), 400
    
    collection.insert_one(user_data)
    return jsonify({"message": "User added successfully"}), 201

# Endpoint for getting all users
@app.route('/users', methods=['GET'])
def get_users():
    users = list(collection.find({}, {"_id": 0}))  # Pobieranie użytkowników bez pola "_id"
    return jsonify(users), 200


if __name__ == '__main__':
    app.run()