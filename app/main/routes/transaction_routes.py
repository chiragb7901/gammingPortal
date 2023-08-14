from flask import Blueprint, current_app,request

from app.main.services.transaction_service import TransactionService
from app.main.services.user_service import token_required

transaction = Blueprint("transaction", __name__)


@transaction.route('/v1/transactions', methods=['GET'])
def get_all_transaction():

    transaction_entities = TransactionService().get_all_transaction_data()

    resp = {
        'status': True,
        'msg': 'Game successfully fetched',
        'data': transaction_entities
    }
    return resp


@transaction.route('/v1/transaction/<id>', methods=['GET'])
def get_transaction_by_id(id):

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
def delete_transaction(id):

    transaction = TransactionService().delete_transaction(id)
    resp = {
        'status': True,
        'msg': 'CreditCard details successfully fetched',
        'data': transaction
    }
    return resp


@transaction.route('/v1/transaction/update/<id>', methods=['PUT'])
def update_transaction(id):
    data = request.get_json()
    transaction = TransactionService().update_transaction(id,data)
    resp = {
        'status': True,
        'msg': 'CreditCard details successfully fetched',
        'data': transaction
    }
    return resp

