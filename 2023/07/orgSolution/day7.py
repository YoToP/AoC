from time import time
from collections import defaultdict, deque
# A, K, Q, J, T, 9, 8, 7, 6, 5, 4, 3, or 2
cardValues = {
  "A": 14,
  "K": 13,
  "Q": 12,
  "J": 11,
  "T": 10,
  "9": 9,
  "8": 8,
  "7": 7,
  "6": 6,
  "5": 5,
  "4": 4,
  "3": 3,
  "2": 2
}
def p1():
    with open("2023/07/inputs/example.txt") as f:
        lines = f.read().split('\n')

    highCardList = deque()
    onePairList = deque()
    twoPairList = deque()
    theeKindList = deque()
    fourKindList = deque()
    FiveKindList = deque()
    for line in lines:
        cards, bid = line.split(' ')
        handData = []
        handData.append(cards)
        handData.append(int(bid))
        cardSet = defaultdict(int)
        for card in cards:
            cardSet[card] += 1
        match len(cardSet):
            case 1: #Five of a kind
                FiveKindList.append(handData)
            case 2: #four of a kind
                fourKindList.append(handData)
            case 3: #three of a kind, or two pair
                highestV = 0
                for k,v, in cardSet.items():
                    if v > highestV:
                        highestV = v
                if highestV == 2:
                    twoPairList.append(handData)
                elif highestV == 3:
                    theeKindList.append(handData)
                else:
                    print(f"Computer says no: {v}")
            case 4: #one pair
                onePairList.append(handData)
            case 5: #high cards/ all diferent
                highCardList.append(handData)
    pass
    rank = 1
    score = 0
    #first lowest
    for hand in highCardList:
        rank += 1

    #one pair
    if len(onePairList) == 1:
        score += onePairList[0][1] * rank
    elif len(onePairList) > 1:
        pass

    #two pair
    if len(twoPairList) == 1:
        score += twoPairList[0][1] * rank
    elif len(twoPairList) > 1:
        i = 0
        highestCard = 0
        while i < len(twoPairList[0][0]):
            cardDict = defaultdict(int)
            for decks in twoPairList:
                if cardValues[twoPairList[0][0][i]] >highestCard:
                    highestCard = cardValues[twoPairList[0][0][i]]
                cardDict[cardValues[decks[0][i]]] += 1
            i+=1
        pass
            
        i+=1
    
    #three kind
    for hand in theeKindList:
        rank += 1

    #four kind
    for hand in fourKindList:
        rank += 1

    #five kind
    for hand in FiveKindList:
        rank += 1
    return lowest


def p2(): 
    
    return 0

if __name__ == '__main__':
    start_time = int(round(time() * 1000))
    print('part 1:', p1())
    print("### p1 run time is %s miliseconds" %
          (int(round(time() * 1000)) - start_time))
    start_time = int(round(time() * 1000))
    print('part 2:', p2())
    print("### p2 run time is %s miliseconds" %
          (int(round(time() * 1000)) - start_time))