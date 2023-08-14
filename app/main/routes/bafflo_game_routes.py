from flask import Blueprint, current_app,request

from app.main.services.bafflo_game_service import BaffloService
from app.main.services.user_service import token_required


bafflo = Blueprint("bafflo", __name__)

@bafflo.route('/v1/game/bafflo/spin/<id>', methods=['POST'])
def spin_game(id):
    data = request.get_json()
    spin_entitiy = BaffloService().spin(id,data)
    resp = {
        'status': True,
        'msg': 'Successful Spin',
        'data': spin_entitiy
    }
    return resp



