# import counter class from collections module
from collections import Counter
with open("2023/07/inputs/input.txt") as f:
    lines = f.read().split('\n')
def strength(hand):
    C = Counter(hand)
    Jcount = C['J']
    hand = hand.replace('T',chr(ord('9')+1))
    hand = hand.replace('J',"1")
    hand = hand.replace('Q',chr(ord('9')+3))
    hand = hand.replace('K',chr(ord('9')+4))
    hand = hand.replace('A',chr(ord('9')+5))
    C = Counter(hand)
    if list(C.values()) == [5]: # five
        return (10,hand)
    elif sorted(C.values()) == [1,4]: #four of akind
        if Jcount == 1:
            return (10, hand)
        else:
            return (9, hand)
    elif sorted(C.values()) == [2,3]: # full house
        if Jcount == 2:
            return (10, hand)
        elif Jcount == 3:
            return (10, hand)
        else:
            return (8, hand)
    elif sorted(C.values()) == [1,1,3]:#three of a kind
        if Jcount == 1:
            return (9, hand)
        elif Jcount == 3:
            return (9, hand)
        else:
            return (7, hand)
    elif sorted(C.values()) == [1,2,2]:#two pair
        if Jcount == 1:
            return (8, hand)
        elif Jcount == 2:
            return (9, hand)
        else:
            return (6, hand)
    elif sorted(C.values()) == [1,1,1,2]:# one pair
        if Jcount == 1:
            return (7, hand)
        elif Jcount == 2:
            return (7, hand)
        else:
            return (5, hand)
    elif sorted(C.values()) == [1,1,1,1,1]:
        if Jcount == 1:
            return (5, hand)
        else:
            return (4, hand)
    else:
        print(f"{C} {hand} {sorted(C.values())}")

H = []
for line in lines:
    hand,bid = line.split(" ")
    H.append((hand,bid))
H = sorted(H, key=lambda hb:strength(hb[0]))

score = 0
for i,(k,v) in enumerate(H):
    score += (i+1)*int(v)
print(score)