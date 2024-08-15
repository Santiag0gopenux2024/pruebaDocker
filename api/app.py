from flask import Flask, request, jsonify, make_response
from pymongo import MongoClient
from redis import Redis
from functools import wraps
from flask_cors import CORS
from config.config import config

import jwt
import datetime
import requests

config_app = config['app']
config_mongo = config['mongo']
config_redis = config['redis']
config_image_service = config['image_service']


app = Flask(__name__)
app.config['SECRET_KEY'] = config_app['secret_key']
CORS(app)

redis_client = Redis(host=config_redis['host'], port=config_redis['port'], db=0, decode_responses=True)

node_service_url = f"http://{config_image_service['host']}:{config_image_service['port']}/random-image"

client = MongoClient(f"mongodb://{config_mongo['host']}:{config_mongo['port']}/")
db = client.user_db
users = db.users


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        if 'x-access-tokens' in request.headers:
            token = request.headers['x-access-tokens']
        
        if not token:
            return jsonify({'message': 'Token is missing!'}), 401

        try:
            data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])
            current_user = users.find_one({'_id': data['user_id']})
        except:
            return jsonify({'message': 'Token is invalid!'}), 401
        
        return f(current_user, *args, **kwargs)
    
    return decorated

@app.route('/login', methods=['POST'])
def login():
    auth = request.json

    if not auth or not auth.get('username') or not auth.get('password'):
        return make_response('Could not verify', 401, {'WWW-Authenticate': 'Basic realm="Login required!"'})

    user = users.find_one({'username': auth['username']})

    if not user:
        return make_response('Could not verify', 401, {'WWW-Authenticate': 'Basic realm="Login required!"'})

    if user['password'] == auth['password']:
        token = jwt.encode({
            'user_id': str(user['_id']),
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
        }, app.config['SECRET_KEY'])
        redis_client.setex(str(user['_id']), 1800, token)
        return jsonify({'token': token})

    return make_response('Could not verify', 403, {'WWW-Authenticate': 'Basic realm="Login required!"'})

@app.route('/user', methods=['POST'])
def create_user():
    data = request.json

    try:
        response = requests.get(node_service_url)
        response.raise_for_status()
        image_url = response.json()['imageUrl']
    except requests.exceptions.RequestException as e:
        print('Error connecting to node service:', e)
        return jsonify({'message': 'Error connecting to image service'}), 500

    new_user = {
        'username': data['username'],
        'password': data['password'],
        'profile_picture': image_url 
    }
    users.insert_one(new_user)
    return jsonify({'message': 'New user created'})

@app.route('/user/<username>', methods=['GET'])
@token_required
def get_user(current_user, username):
    user = users.find_one({'username': username})

    if user:
        user_data = {
            'id': str(user['_id']),
            'username': user['username'],
            'profile_picture': user['profile_picture']
        }
        return jsonify(user_data)
    else:
        return jsonify({'message': 'User not found'})

@app.route('/user', methods=['GET'])
def get_all_users():
    all_users = users.find({})
    result = []
    for user in all_users:
        user_data = {
            'id': str(user['_id']),
            'username': user['username'],
            'profile_picture': user['profile_picture']
        }
        result.append(user_data)
    return jsonify(result)

if __name__ == '__main__':
    config_app = config['app']
    app.run(port=config_app['port'], debug=config_app['debug'], host=config_app['host'])
