import random
import numpy as np

# Receive the bid price from player 1 and player 2

# Return a 2x2 list, 
# each 2-tuple includes the allocation result (i.e., a flag indicating whether you win the item), and your payment

# If there is a tie, make a random winner 
def auctionStrategy(bid1, bid2):
    if bid1 > bid2:
        return [[1, bid1],[0,bid2]]
    elif bid1 < bid2:
        return [[0,bid1],[1, bid2]]
    else:
        if random.uniform(0,1) <0.5:
            return [[1, bid1], [0,bid2]]
        else:
            return [[0,bid1], [1, bid2]]
