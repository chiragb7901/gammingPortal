import random
from itertools import combinations
from itertools import product

combinations_set = {'D', 'C', 'G', 'E', 'B', 'M', 'A', 'K', 'Q', 'J', 'F'}
comb_size = 3

valid_combinations = [combo for combo in product(combinations_set, repeat=comb_size)]
random_combination = random.choice(valid_combinations)
print("Randomly selected combination:", ' '.join(random_combination))  

combinations = {"DDD", "CCC", "GGG", "EEE", "BBB", "MMM", "AAA", "KKK", "QQQ", "JJJ", "FFF"}
probabilities = [0.02  ,0.09,  0.1,   0.11,  0.14  ,0.17,  0.2,   0.21,  0.31,   0.3,  0.4]
def spin_slot_machine():
    outcome = random.choices(list(combinations), probabilities)[0]
    return outcome

# outcome = spin_slot_machine()
# print(f"Spinning... The result is: {outcome}")
check =  "".join(random_combination)
if check in combinations:
    print("match!!!")


maping = {
    'B3':'C',
    'B2':'G',
    'B1':'E',
    '10':'F',
    'bull':'M',
}