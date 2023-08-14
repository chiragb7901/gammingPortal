from flask import Blueprint, current_app,request

from app.main.services.role_service import RoleService
from app.main.services.user_service import token_required

role = Blueprint("role", __name__)


@role.route('/v1/roles', methods=['GET'])
def get_all_role():

    role_entities = RoleService().get_all_role_data()

    resp = {
        'status': True,
        'msg': 'Game successfully fetched',
        'data': role_entities
    }
    return resp


@role.route('/v1/role/<id>', methods=['GET'])
def get_role_by_id(id):

    role_entities = RoleService().get_role_by_id(id=id)

    resp = {
        'status': True,
        'msg': 'Game successfully fetched',
        'data': role_entities
    }
    return resp

@role.route('/v1/role', methods=['POST'])
def save_new_role():
    data = request.get_json()
    role_entities = RoleService().save_new_role(data)
    resp = {
        'status': True,
        'msg': 'CreditCard details successfully fetched',
        'data': role_entities
    }
    return resp

@role.route('/v1/role/delete/<id>', methods=['DELETE'])
def delete_role(id):

    role = RoleService().delete_role(id)
    resp = {
        'status': True,
        'msg': 'CreditCard details successfully fetched',
        'data': role
    }
    return resp


@role.route('/v1/role/update/<id>', methods=['PUT'])
def update_role(id):
    data = request.get_json()
    role = RoleService().update_role(id,data)
    resp = {
        'status': True,
        'msg': 'CreditCard details successfully fetched',
        'data': role
    }
    return resp

