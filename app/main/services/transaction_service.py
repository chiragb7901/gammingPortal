from app.main.models import Transaction


class TransactionService:
    def __init__(self):
        pass

    @staticmethod
    def get_all_transaction_data():
        transaction_entities = Transaction.query.all()
        transaction_entities_list = []
        
        for user in transaction_entities:
            transaction_dict = {}
            transaction_dict['id'] = user.id
            transaction_dict['user_id'] = user.user_id
            transaction_dict['game_id'] = user.game_id
            transaction_dict['bid_price'] = user.bid_price
            transaction_dict['result'] = user.result
            transaction_dict['price'] = user.price
            transaction_dict['created_at'] = user.created_at
            transaction_dict['updated_at'] = user.updated_at
           
            transaction_entities_list.append(transaction_dict)
        return transaction_entities_list

    @staticmethod
    def get_transaction_by_id(id):
        transaction_entities = Transaction.query.filter_by(id=id)
        transaction_entities_list = []

        for user in transaction_entities:
            transaction_dict = {}
            transaction_dict['id'] = user.id
            transaction_dict['user_id'] = user.user_id
            transaction_dict['game_id'] = user.game_id
            transaction_dict['bid_price'] = user.bid_price
            transaction_dict['result'] = user.result
            transaction_dict['price'] = user.price
            transaction_dict['created_at'] = user.created_at
            transaction_dict['updated_at'] = user.updated_at

            transaction_entities_list.append(transaction_dict)
        return transaction_entities_list
    


    @staticmethod
    def save_new_transaction(data):

        new_transaction = Transaction(
                user_id=data["user_id"],
                game_id=data["game_id"],
                bid_price=data["bid_price"],
                result=data["result"],
                price=data["price"]
        )
        new = Transaction.create(new_transaction)
        response_object = {
                "status": "success",
                "object":{
                    "user_id":new.user_id,
                    "game_id":new.game_id,
                    "bid_price":new.bid_price,
                    "result":new.result,
                    "price":new.price,
                    "id":new.id

                },
                "message": "Successfully added.",
        }
        return response_object, 201

        

    @staticmethod
    def delete_transaction(id):
        transaction= Transaction.query.filter_by(id=id).first()
        
        if transaction:
            Transaction.delete(transaction)
            response_object = {
                "status": "success",
                "message": "Successfully deleted.",
            }
            return response_object, 201
        else:
            response_object = {
                "status": "fail",
                "message": "transaction does not exists.",
            }
            return response_object, 409     

    @staticmethod
    def update_transaction(id,data):
        
        transactionNew = Transaction.query.filter_by(id=id).first()

    
        if transactionNew:

            transactionNew.user_id = data.get('game', transactionNew.user_id)
            transactionNew.game_id = data.get('game', transactionNew.game_id)
            transactionNew.bid_price = data.get('game', transactionNew.bid_price)
            transactionNew.result = data.get('game', transactionNew.result)
            transactionNew.price = data.get('game', transactionNew.price)

            new = Transaction.update(transactionNew)
            response_object = {
                "status": "success",
                "object":{
                    "user_id":new.user_id,
                    "game_id":new.game_id,
                    "bid_price":new.bid_price,
                    "result":new.result,
                    "price":new.price,
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

