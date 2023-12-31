from flask import Blueprint, current_app,request

from app.main.services.game_service import GameService
from app.main.services.user_service import token_required

game = Blueprint("game", __name__)


@game.route('/v1/games', methods=['GET'])
def get_all_game():

    game_entities = GameService().get_all_Game_data()

    resp = {
        'status': True,
        'msg': 'Game successfully fetched',
        'data': game_entities
    }
    return resp


@game.route('/v1/games/<id>', methods=['GET'])
def get_game_by_id(id):

    game_entities = GameService().get_Game_by_id(id=id)

    resp = {
        'status': True,
        'msg': 'Game successfully fetched',
        'data': game_entities
    }
    return resp

@game.route('/v1/game', methods=['POST'])
def save_new_game():
    data = request.get_json()
    game_entities = GameService().save_new_Game(data)
    resp = {
        'status': True,
        'msg': 'CreditCard details successfully fetched',
        'data': game_entities
    }
    return resp



@game.route('/v1/game/delete/<id>', methods=['DELETE'])
def delete_game(id):

    game = GameService().delete_Game(id)
    resp = {
        'status': True,
        'msg': 'CreditCard details successfully fetched',
        'data': game
    }
    return resp


@game.route('/v1/game/update/<id>', methods=['PUT'])
def update_game(id):
    data = request.get_json()
    game = GameService().update_game(id,data)
    resp = {
        'status': True,
        'msg': 'CreditCard details successfully fetched',
        'data': game
    }
    return resp

