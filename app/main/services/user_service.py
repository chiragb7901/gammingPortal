from app.main.models import User
import jwt
import uuid 
from datetime import datetime, timedelta
from functools import wraps
from flask import request,jsonify
from app.main.settings import Config


class UserService:
    def __init__(self):
        pass
 
    @staticmethod
    def get_all_user_data():
        user_entities = User.query.all()
        user_entities_list = []
        
        for user in user_entities:
            user_dict = {}
            user_dict['username'] = user.username
            user_dict['id'] = user.id
            user_dict['public_id'] = user.public_id
            user_dict['created_at'] = user.created_at
            user_dict['updated_at'] = user.updated_at
            user_dict['password'] = user.password
            user_dict['role'] = user.role
            user_dict['balance'] = user.balance
            
            user_entities_list.append(user_dict)
        return user_entities_list
    
 
    @staticmethod
    def get_user_by_id(id):
        user_entities = User.query.filter_by(id=id)
        user_entities_list = []

        for user in user_entities:
            user_dict = {}
            user_dict['username'] = user.username
            user_dict['id'] = user.id
            user_dict['public_id'] = user.public_id
            user_dict['created_at'] = user.created_at
            user_dict['updated_at'] = user.updated_at
            user_dict['password'] = user.password
            user_dict['role'] = user.role
            user_dict['balance'] = user.balance
            
            user_entities_list.append(user_dict)
        return user_entities_list


    @staticmethod
    def save_new_user(data):
        user = User.query.filter_by(username=data["username"]).first()
        if not user:
            new_user = User(
                public_id = str(uuid.uuid4()),
                username=data["username"],
                role="User",
                balance=0,
                password=data["password"]
            )
            new = User.create(new_user)
            response_object = {
                "status": "success",
                "object":{
                    "username":new.username,
                    "role":new.role,
                    "password":new.password,
                    "balance":new.balance,
                    "id":new.id,

                },
                "message": "Successfully added.",
            }
            return response_object, 201
        else:
            response_object = {
                "status": "fail",
                "message": "Email already exists. Please use new one.",
            }
            return response_object, 409
        


    @staticmethod
    def delete_user(id):
        user= User.query.filter_by(id=id).first()
        
        if user:
            User.delete(user)
            response_object = {
                "status": "success",
                "message": "Successfully deleted.",
            }
            return response_object, 201
        else:
            response_object = {
                "status": "fail",
                "message": "User does not exists.",
            }
            return response_object, 409
        

    @staticmethod
    def update_user(id,data):
        user= User.query.filter_by(id=id).first()
        
        if user:
            user.username = data.get('username', user.username)
            user.password = data.get('password', user.password)
            user.role = data.get('role', user.role)
            user.balance = data.get('balance', user.balance)
        
            new = User.update(user)
            response_object = {
                "status": "success",
                "object":{
                    "username":new.username,
                    "password":new.password,
                    "role":new.role,
                    "id":new.id,
                    "balance":new.balance,

                },
                "message": "Successfully updated.",
            }
            return response_object, 201
        else:
            response_object = {
                "status": "fail",
                "message": "User details not found.",
            }
            return response_object, 409
    
    
        
    @staticmethod
    def login(auth):
    
        if not auth or not auth.get('username') or not auth.get('password'):
            response_object = {
                "test":"details not found",
                "status": "fail",
                "message": 'Could not verify',
                "status_code":401,
                'WWW-Authenticate' : 'Basic realm ="Login required !!"'
            }
            return response_object
    
        user = User.query.filter_by(username = auth.get('username'))\
            .first()
    
        if not user:
            response_object = {
                "test":"user not found",
                "status": "fail",
                "message": 'Could not verify',
                "status_code":401,
                'WWW-Authenticate' : 'Basic realm ="Login required !!"'
            }
            return response_object
        
        if (user.password==auth.get('password')):
           
            token = jwt.encode({
                'public_id': user.public_id,
                'exp' : datetime.utcnow() + timedelta(minutes = 120)
            }, Config.SECRET_KEY)

            response_object = {
                'id':user.id,
                'token' : token 
            }
            return response_object
        
        else:
            response_object= {
                'WWW-Authenticate' : 'Basic realm ="Wrong Password !!"',
                "status_code":403,
                'msg':"InCorrect Password"
                }
            return response_object
    

        
        
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']
        if not token:
            return jsonify({'message' : 'Token is missing !!'}), 401
  
        try:
            data = jwt.decode(token, Config.SECRET_KEY, algorithms=['HS256'])
            current_user = User.query\
                .filter_by(public_id = data['public_id'])\
                .first()
        except:
            return jsonify({
                'message' : 'Token is invalid !!'
            }), 401
        return  f(current_user, *args, **kwargs)
  
    return decorated