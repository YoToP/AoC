from time import time
from collections import Counter

def replaceCards(cards):
    cards = cards.replace('T',chr(ord('9')+1))
    cards = cards.replace('J',chr(ord('9')+2))
    cards = cards.replace('Q',chr(ord('9')+3))
    cards = cards.replace('K',chr(ord('9')+4))
    cards = cards.replace('A',chr(ord('9')+5))
    return cards

def replaceCardsP2(cards):
    cards = cards.replace('T',chr(ord('9')+1))
    cards = cards.replace('J','0')
    cards = cards.replace('Q',chr(ord('9')+3))
    cards = cards.replace('K',chr(ord('9')+4))
    cards = cards.replace('A',chr(ord('9')+5))
    return cards

def p1():
    with open("2023/07/inputs/input.txt") as f:
        lines = f.read().split('\n')

    strength = []
    for line in lines:
        cards, bid = line.split(' ')
        cardSet = Counter(cards)
        a = list(cardSet.values())

        match len(cardSet):
            case 1: #Five of a kind
                strength.append((((6,replaceCards(cards)),bid)))
            case 2: #four of a kind or full house
                if sorted(a, reverse=True)[0] == 4:
                    strength.append((((5,replaceCards(cards)),bid)))
                if sorted(a, reverse=True)[0] == 3:
                    strength.append((((4,replaceCards(cards)),bid)))                
            case 3: #three of a kind, or two pair
                if sorted(a, reverse=True)[0] == 2:
                    strength.append((((2,replaceCards(cards)),bid)))
                if sorted(a, reverse=True)[0] == 3:
                    strength.append((((3,replaceCards(cards)),bid)))
            case 4: #one pair
                strength.append((((1,replaceCards(cards)),bid)))
            case 5: #high cards/ all diferent
                strength.append((((0,replaceCards(cards)),bid)))
    sortedList = sorted(strength, key=lambda b:b[0])

    score = 0
    for i,(_,bid) in enumerate(sortedList,1):
        score += i*int(bid)
    return score


def p2(): 
    with open("2023/07/inputs/input.txt") as f:
        lines = f.read().split('\n')

    strength = []
    for line in lines:
        cards, bid = line.split(' ')
        cards = replaceCardsP2(cards)
        cardSet = Counter(cards)

        # sort the deck to have the highest count card fist, and replace all J with this card.
        if '0' in cardSet:
            #check for amounts in the counter
            maxValue = 0
            keyList = []
            for k,v in cardSet.items():
                if k == '0': # Exclude J
                    continue
                if v > maxValue:
                    maxValue = v
                    keyList.clear()
                    keyList.append(k)
                elif v == maxValue:
                    keyList.append(k)
            if len(keyList) > 0: # edge case if all cards are J, then the list is empty
                highKey = max(keyList)
                cardSet[highKey] += cardSet['0']
                cardSet.pop('0')
        a = list(cardSet.values())
            
        match len(cardSet):
            case 1: #Five of a kind
                strength.append((((6,cards),bid)))
            case 2: #four of a kind or full house
                if sorted(a, reverse=True)[0] == 4:
                    strength.append((((5,cards),bid)))
                elif sorted(a, reverse=True)[0] == 3:
                    strength.append((((4,cards),bid)))    
                else:
                    pass            
            case 3: #three of a kind, or two pair
                if sorted(a, reverse=True)[0] == 2:
                    strength.append((((2,cards),bid)))
                elif sorted(a, reverse=True)[0] == 3:
                    strength.append((((3,cards),bid)))
                else:
                    pass
            case 4: #one pair
                strength.append((((1,cards),bid)))
            case 5: #high cards/ all diferent
                strength.append((((0,cards),bid)))
    sortedList = sorted(strength, key=lambda b:b[0])
    score = 0
    for i,(_,bid) in enumerate(sortedList,1):
        score += i*int(bid)
    return score

if __name__ == '__main__':
    start_time = int(round(time() * 1000))
    print('part 1:', p1())
    print("### p1 run time is %s miliseconds" %
          (int(round(time() * 1000)) - start_time))
    start_time = int(round(time() * 1000))
    print('part 2:', p2())
    print("### p2 run time is %s miliseconds" %
          (int(round(time() * 1000)) - start_time))