from flask import Blueprint, current_app,request

from app.main.services.user_service import UserService,token_required

user = Blueprint("user", __name__)


@user.route('/v1/users', methods=['GET'])
def get_all_user():

    user_entities = UserService().get_all_user_data()

    resp = {
        'status': True,
        'msg': 'Users successfully fetched',
        'data': user_entities
    }
    return resp


@user.route('/v1/user/<id>', methods=['GET'])
def get_user_by_id(id):

    user_entities = UserService().get_user_by_id(id=id)

    resp = {
        'status': True,
        'msg': 'Users successfully fetched',
        'data': user_entities
    }
    return resp

@user.route('/v1/signup', methods=['POST'])
def save_new_user():
    data = request.get_json()
    user_entities = UserService().save_new_user(data)
    resp = {
        'status': True,
        'msg': 'CreditCard details successfully fetched',
        'data': user_entities
    }
    return resp


@user.route('/v1/login', methods=['POST'])
def login():
    data = request.get_json()
    login_entity = UserService().login(data)
    resp = {
        'status': True,
        'data': login_entity
    }
    return resp


@user.route('/v1/user/delete/<id>', methods=['DELETE'])
def delete_creditcard(id):

    user = UserService().delete_user(id)
    resp = {
        'status': True,
        'msg': 'CreditCard details successfully fetched',
        'data': user
    }
    return resp


@user.route('/v1/user/update/<id>', methods=['PUT'])
def update_creditcard(id):
    data = request.get_json()
    user = UserService().update_user(id,data)
    resp = {
        'status': True,
        'msg': 'CreditCard details successfully fetched',
        'data': user
    }
    return resp

