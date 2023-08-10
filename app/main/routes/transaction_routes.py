from flask import Blueprint, current_app,request

from app.main.services.transaction_service import TransactionService
from app.main.services.user_service import token_required

transaction = Blueprint("transaction", __name__)


@transaction.route('/v1/transactions', methods=['GET'])
@token_required
def get_all_transaction(current_user):

    transaction_entities = TransactionService().get_all_transaction_data()

    resp = {
        'status': True,
        'msg': 'Game successfully fetched',
        'data': transaction_entities
    }
    return resp


@transaction.route('/v1/transaction/<id>', methods=['GET'])
@token_required
def get_transaction_by_id(current_user,id):

    transaction_entities = TransactionService().get_transaction_by_id(id=id)

    resp = {
        'status': True,
        'msg': 'Game successfully fetched',
        'data': transaction_entities
    }
    return resp

@transaction.route('/v1/transaction', methods=['POST'])
def save_new_transaction():
    data = request.get_json()
    transaction_entities = TransactionService().save_new_transaction(data)
    resp = {
        'status': True,
        'msg': 'CreditCard details successfully fetched',
        'data': transaction_entities
    }
    return resp

@transaction.route('/v1/transaction/delete/<id>', methods=['DELETE'])
@token_required
def delete_transaction(current_user,id):

    transaction = TransactionService().delete_transaction(id)
    resp = {
        'status': True,
        'msg': 'CreditCard details successfully fetched',
        'data': transaction
    }
    return resp


@transaction.route('/v1/transaction/update/<id>', methods=['PUT'])
@token_required
def update_transaction(current_user,id):
    data = request.get_json()
    transaction = TransactionService().update_transaction(id,data)
    resp = {
        'status': True,
        'msg': 'CreditCard details successfully fetched',
        'data': transaction
    }
    return resp

