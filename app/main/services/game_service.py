from app.main.models import Game


class GameService:
    def __init__(self):
        pass

    @staticmethod
    def get_all_Game_data():
        game_entities = Game.query.all()
        game_entities_list = []
        
        for user in game_entities:
            game_dict = {}
            game_dict['id'] = user.id
            game_dict['game'] = user.game
            game_dict['game_code'] = user.game_code
            game_dict['created_at'] = user.created_at
            game_dict['updated_at'] = user.updated_at
           
            game_entities_list.append(game_dict)
        return game_entities_list

    @staticmethod
    def get_Game_by_id(id):
        game_entities = Game.query.filter_by(id=id)
        game_entities_list = []

        for user in game_entities:
            game_dict = {}
            game_dict['id'] = user.id
            game_dict['game'] = user.game
            game_dict['game_code'] = user.game_code
            game_dict['created_at'] = user.created_at
            game_dict['updated_at'] = user.updated_at

            game_entities_list.append(game_dict)
        return game_entities_list
    


    @staticmethod
    def save_new_Game(data):

        new_game = Game(
                game=data["game"],
                game_code=data["game_code"]
        )
        new = Game.create(new_game)
        response_object = {
                "status": "success",
                "object":{
                    "game":new.game,
                    "game_code":new.game_code,
                    "id":new.id

                },
                "message": "Successfully added.",
        }
        return response_object, 201

        

    @staticmethod
    def delete_Game(id):
        game= Game.query.filter_by(id=id).first()
        
        if game:
            Game.delete(game)
            response_object = {
                "status": "success",
                "message": "Successfully deleted.",
            }
            return response_object, 201
        else:
            response_object = {
                "status": "fail",
                "message": "game does not exists.",
            }
            return response_object, 409     

    @staticmethod
    def update_game(id,data):
        
        gameNew = Game.query.filter_by(id=id).first()

    
        if gameNew:

            gameNew.game = data.get('game', gameNew.game)
            gameNew.game_code = data.get('game_code', gameNew.game_code)

            new = Game.update(gameNew)
            response_object = {
                "status": "success",
                "object":{
                    "game":new.game,
                    "game_code":new.game_code,
                    "id":new.id

                },
                "message": "Successfully updated.",
            }
            return response_object, 201
        else:
            response_object = {
                "status": "fail",
                "message": "Card does not exists.",
            }
            return response_object, 409

