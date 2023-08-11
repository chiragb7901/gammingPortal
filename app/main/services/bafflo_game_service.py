from app.main.services.transaction_service import TransactionService
from app.main.services.user_service import UserService
import random
from itertools import product

class BaffloService:
    def __init__(self):
        pass
    
    @staticmethod
    def spin(data):
        bid = data.bid_price
        combinations_set = {'D', 'C', 'G', 'E', 'B', 'M', 'A', 'K', 'Q', 'J', 'F'}
        comb_size = 3
        
        combinations = {"DDD", "CCC", "GGG", "EEE", "BBB", "MMM", "AAA", "KKK", "QQQ", "JJJ", "FFF"}
        valid_combinations = [combo for combo in product(combinations_set, repeat=comb_size)]
        random_combination = random.choice(valid_combinations)
        print("Randomly selected combination:", ' '.join(random_combination))     
        check =  "".join(random_combination)
        maping = {
            'B3':'C',
            'B2':'G',
            'B1':'E',
            '10':'F',
            'bull':'M',
        }
        win = "Loss"
        win_amount = 0;
        user_info = UserService.get_user_by_id(data.user_id)
        if check in combinations:
            win = "Win"
            if check=="DDD":
                win_amount = bid * 250
            if check=="CCC":
                win_amount = bid * 100
            if check=="GGG":
                win_amount = bid * 75
            if check=="EEE":
                win_amount = bid * 50
            if check=="BBB":
                win_amount = bid * 15
            if check=="MMM":
                win_amount = bid * 10
            if check=="AAA":
                win_amount = bid * 5
            if check=="KKK":
                win_amount = bid * 4
            if check=="QQQ":
                win_amount = bid * 3
            if check=="JJJ":
                win_amount = bid * 2
            if check=="FFF":
                win_amount = bid * 1
            finalBal = win_amount-bid
            change = {
                "balance":finalBal
            }
            finalBal = user_info.balance +win_amount - bid
            rev = {
                "balance":finalBal
            }
            UserService.update_user(data.user_id,rev)
        if win_amount==0:
            finalBal = user_info.balance +win_amount - bid
            rev = {
                "balance":finalBal
            }
            UserService.update_user(data.user_id,rev)
        resp={
                    "user_id":data.user_id,
                    "game_id":1,
                    "result":win,
                    "price": win_amount,
                    "bid_price":bid
                }
        response_object = TransactionService.save_new_transaction(resp)
    
        return response_object, 201