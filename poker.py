import random
import os


def one_pair(hand):         # Jack or better, returns boolean
    pairs = []
    for i in range(4):
        first_card = hand[i]
        for j in range(1, 5):
            second_card = hand[j]
            if i != j:
                if first_card["value"] == second_card["value"]:
                    if first_card not in pairs:
                        if first_card["value"] >= 11 or first_card["value"] == 1:
                            pairs.append(first_card)
                            pairs.append(second_card)
                            return True


def two_pair(hand):
    pairs = []
    for i in range(4):
        first_card = hand[i]
        for j in range(1, 5):
            second_card = hand[j]
            if i != j:
                if first_card["value"] == second_card["value"]:
                    if first_card["value"] not in pairs:
                        pairs.append(first_card["value"])
                        pairs.append(second_card["value"])
    if len(pairs) == 4:
        return True


def three_of_a_kind(hand):
    three_of_a_kind = []
    for i in range(5):
        first_card = hand[i]
        for j in range(5):
            second_card = hand[j]
            for k in range(5):
                third_card = hand[k]
                if i != j and j != k and i != k:
                    if first_card["value"] == second_card["value"] and second_card["value"] == third_card["value"] and first_card["value"] == third_card["value"]:
                        if first_card not in three_of_a_kind and second_card not in three_of_a_kind:
                            three_of_a_kind.append(first_card)
                            three_of_a_kind.append(second_card)
                            three_of_a_kind.append(three_of_a_kind)
                            return True


def straight(hand):
    straight = []
    ace_to_ten = [1, 10, 11, 12, 13]
    straight_check = 0
    for i in range(5):
        card = hand[i]
        straight.append(card["value"])
        straight.sort()
    for i in range(4):
        if straight[i + 1] - straight[i] == 1:
            straight_check += 1
    if straight_check == 4:
        return True
    if straight == ace_to_ten:
        return True


def flush(hand):
    card_colors = []
    for i in range(5):
        card = hand[i]
        card_colors.append(card["color"])
    card_colors_set = set(card_colors)
    if len(card_colors_set) == 1:
        return True


def full_house(hand):
    fh_check = []
    for i in range(5):
        card = hand[i]
        fh_check.append(card["value"])
    fh_check_set = set(fh_check)
    if len(fh_check_set) == 2:
        return True


def four_of_a_kind(hand):
    four_of_a_kind_check = []
    for i in range(5):
        card = hand[i]
        four_of_a_kind_check.append(card["value"])
    for i in range(1, 14):
        if four_of_a_kind_check.count(i) == 4:
            return True


def straight_flush(hand):
    if straight(hand) and flush(hand):
        return True


def royal_flush(hand):
    royal_flush = {1, 10, 11, 12, 13}
    royal_flush_color = []
    royal_flush_value = []
    for i in range(5):
        card = hand[i]
        royal_flush_color.append(card["color"])
        royal_flush_value.append(card["value"])
    royal_flush_set_value = set(royal_flush_value)
    royal_flush_set_color = len(set(royal_flush_color))
    if royal_flush_set_color == 1 and royal_flush_set_value == royal_flush:
        return True


def cards():           # Creates card dictionary
    s_a = {"face": "\033[1;32;49m🂡\033[0m", "value": 1, "color": "spades"}
    s_2 = {"face": "\033[1;32;49m🂢\033[0m", "value": 2, "color": "spades"}
    s_3 = {"face": "\033[1;32;49m🂣\033[0m", "value": 3, "color": "spades"}
    s_4 = {"face": "\033[1;32;49m🂤\033[0m", "value": 4, "color": "spades"}
    s_5 = {"face": "\033[1;32;49m🂥\033[0m", "value": 5, "color": "spades"}
    s_6 = {"face": "\033[1;32;49m🂦\033[0m", "value": 6, "color": "spades"}
    s_7 = {"face": "\033[1;32;49m🂧\033[0m", "value": 7, "color": "spades"}
    s_8 = {"face": "\033[1;32;49m🂨\033[0m", "value": 8, "color": "spades"}
    s_9 = {"face": "\033[1;32;49m🂩\033[0m", "value": 9, "color": "spades"}
    s_10 = {"face": "\033[1;32;49m🂪\033[0m", "value": 10, "color": "spades"}
    s_j = {"face": "\033[1;32;49m🂫\033[0m", "value": 11, "color": "spades"}
    s_q = {"face": "\033[1;32;49m🂭\033[0m", "value": 12, "color": "spades"}
    s_k = {"face": "\033[1;32;49m🂮\033[0m", "value": 13, "color": "spades"}

    h_a = {"face": "\033[1;31;49m🂱\033[0m", "value": 1, "color": "hearts"}
    h_2 = {"face": "\033[1;31;49m🂲\033[0m", "value": 2, "color": "hearts"}
    h_3 = {"face": "\033[1;31;49m🂳\033[0m", "value": 3, "color": "hearts"}
    h_4 = {"face": "\033[1;31;49m🂴\033[0m", "value": 4, "color": "hearts"}
    h_5 = {"face": "\033[1;31;49m🂵\033[0m", "value": 5, "color": "hearts"}
    h_6 = {"face": "\033[1;31;49m🂶\033[0m", "value": 6, "color": "hearts"}
    h_7 = {"face": "\033[1;31;49m🂷\033[0m", "value": 7, "color": "hearts"}
    h_8 = {"face": "\033[1;31;49m🂸\033[0m", "value": 8, "color": "hearts"}
    h_9 = {"face": "\033[1;31;49m🂹\033[0m", "value": 9, "color": "hearts"}
    h_10 = {"face": "\033[1;31;49m🂺\033[0m", "value": 10, "color": "hearts"}
    h_j = {"face": "\033[1;31;49m🂻\033[0m", "value": 11, "color": "hearts"}
    h_q = {"face": "\033[1;31;49m🂽\033[0m", "value": 12, "color": "hearts"}
    h_k = {"face": "\033[1;31;49m🂾\033[0m", "value": 13, "color": "hearts"}

    d_a = {"face": "\033[1;33;49m🃁\033[0m", "value": 1, "color": "diamonds"}
    d_2 = {"face": "\033[1;33;49m🃂\033[0m", "value": 2, "color": "diamonds"}
    d_3 = {"face": "\033[1;33;49m🃃\033[0m", "value": 3, "color": "diamonds"}
    d_4 = {"face": "\033[1;33;49m🃄\033[0m", "value": 4, "color": "diamonds"}
    d_5 = {"face": "\033[1;33;49m🃅\033[0m", "value": 5, "color": "diamonds"}
    d_6 = {"face": "\033[1;33;49m🃆\033[0m", "value": 6, "color": "diamonds"}
    d_7 = {"face": "\033[1;33;49m🃇\033[0m", "value": 7, "color": "diamonds"}
    d_8 = {"face": "\033[1;33;49m🃈\033[0m", "value": 8, "color": "diamonds"}
    d_9 = {"face": "\033[1;33;49m🃉\033[0m", "value": 9, "color": "diamonds"}
    d_10 = {"face": "\033[1;33;49m🃊\033[0m", "value": 10, "color": "diamonds"}
    d_j = {"face": "\033[1;33;49m🃋\033[0m", "value": 11, "color": "diamonds"}
    d_q = {"face": "\033[1;33;49m🃍\033[0m", "value": 12, "color": "diamonds"}
    d_k = {"face": "\033[1;33;49m🃎\033[0m", "value": 13, "color": "diamonds"}

    c_a = {"face": "\033[1;34;49m🃑\033[0m", "value": 1, "color": "clubs"}
    c_2 = {"face": "\033[1;34;49m🃒\033[0m", "value": 2, "color": "clubs"}
    c_3 = {"face": "\033[1;34;49m🃓\033[0m", "value": 3, "color": "clubs"}
    c_4 = {"face": "\033[1;34;49m🃔\033[0m", "value": 4, "color": "clubs"}
    c_5 = {"face": "\033[1;34;49m🃕\033[0m", "value": 5, "color": "clubs"}
    c_6 = {"face": "\033[1;34;49m🃖\033[0m", "value": 6, "color": "clubs"}
    c_7 = {"face": "\033[1;34;49m🃗\033[0m", "value": 7, "color": "clubs"}
    c_8 = {"face": "\033[1;34;49m🃘\033[0m", "value": 8, "color": "clubs"}
    c_9 = {"face": "\033[1;34;49m🃙\033[0m", "value": 9, "color": "clubs"}
    c_10 = {"face": "\033[1;34;49m🃚\033[0m", "value": 10, "color": "clubs"}
    c_j = {"face": "\033[1;34;49m🃛\033[0m", "value": 11, "color": "clubs"}
    c_q = {"face": "\033[1;34;49m🃝\033[0m", "value": 12, "color": "clubs"}
    c_k = {"face": "\033[1;34;49m🃞\033[0m", "value": 13, "color": "clubs"}

    deck = [s_a, s_2, s_3, s_4, s_5, s_6, s_7, s_8, s_9, s_10, s_j, s_q, s_k,
            h_a, h_2, h_3, h_4, h_5, h_6, h_7, h_8, h_9, h_10, h_j, h_q, h_k,
            d_a, d_2, d_3, d_4, d_5, d_6, d_7, d_8, d_9, d_10, d_j, d_q, d_k,
            c_a, c_2, c_3, c_4, c_5, c_6, c_7, c_8, c_9, c_10, c_j, c_q, c_k]
    
    return deck


def hold(hand, deck):
    hold_list = []
    cards_to_hold = str(input("Which card(s) to hold? (1-5): "))
    print("Invalid input")
    for i in cards_to_hold:
        hold_list.append(int(i))
    for i in range(5):
        j = i + 1
        if j not in hold_list:
            current_card = random.choice(deck)
            if current_card not in hand:
                hand[i] = current_card
    return hand


def deal(deck, hold_list):                # Deals 5 unique cards
    dealt_cards = []
    while len(dealt_cards) != 5:
        current_card = random.choice(deck)
        if current_card not in dealt_cards:
            dealt_cards.append(current_card)
    return dealt_cards


def hand_evaluate(hand):
    if royal_flush(hand):
        hand_result = "ROYAL FLUSH"
    elif straight_flush(hand):
        hand_result = "STRAIGHT FLUSH"
    elif four_of_a_kind(hand):
        hand_result = "FOUR OF A KIND"
    elif full_house(hand):
        hand_result = "FULL HOUSE"
    elif flush(hand):
        hand_result = "FLUSH"
    elif straight(hand):
        hand_result = "STRAIGHT"
    elif three_of_a_kind(hand):
        hand_result = "THREE OF A KIND"
    elif two_pair(hand):
        hand_result = "TWO PAIR"
    elif one_pair(hand):
        hand_result = "JACKS OR BETTER"
    else:
        hand_result = "NOTHING"
    return hand_result


def payout_table(credit):
    print(f'''
/-----------------------------\ 
|ROYAL FLUSH...............250|
|STRAIGHT FLUSH............ 50|
|FOUR OF A KIND.............25|
|FULL HOUSE..................9|
|FLUSH.......................6|
|STRAIGHT....................4|
|THREE OF A KIND.............3|
|TWO PAIR....................2|
|JACKS OR BETTER.............1|
|-----------------------------|
|CREDIT: {credit}                  |    
\-----------------------------/
''')


def intro():
    print('''
 ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ 
     ██╗ █████╗  ██████╗██╗  ██╗███████╗     ██████╗ ██████╗     ██████╗ ███████╗████████╗████████╗███████╗██████╗ 
     ██║██╔══██╗██╔════╝██║ ██╔╝██╔════╝    ██╔═══██╗██╔══██╗    ██╔══██╗██╔════╝╚══██╔══╝╚══██╔══╝██╔════╝██╔══██╗
     ██║███████║██║     █████╔╝ ███████╗    ██║   ██║██████╔╝    ██████╔╝█████╗     ██║      ██║   █████╗  ██████╔╝
██   ██║██╔══██║██║     ██╔═██╗ ╚════██║    ██║   ██║██╔══██╗    ██╔══██╗██╔══╝     ██║      ██║   ██╔══╝  ██╔══██╗
╚█████╔╝██║  ██║╚██████╗██║  ██╗███████║    ╚██████╔╝██║  ██║    ██████╔╝███████╗   ██║      ██║   ███████╗██║  ██║
 ╚════╝ ╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝     ╚═════╝ ╚═╝  ╚═╝    ╚═════╝ ╚══════╝   ╚═╝      ╚═╝   ╚══════╝╚═╝  ╚═╝
 ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ 
''')


def credit(result, credit):
    if result == "ROYAL FLUSH":
        credit += 250
    if result == "STRAIGHT FLUSH":
        credit += 50
    if result == "FOUR OF A KIND":
        credit += 25
    if result == "FULL HOUSE":
        credit += 9
    if result == "FLUSH":
        credit += 6
    if result == "STRAIGHT":
        credit += 4
    if result == "THREE OF A KIND":
        credit += 3
    if result == "TWO PAIR":
        credit += 2
    if result == "JACKS OR BETTER":
        credit += 1
    if result == "NOTHING":
        credit -= 1
    return credit
        
    
def main():
    os.system("clear")
    intro()
    money_credit = 200
    hold_list = []
    deck = cards()
    hand = deal(deck, hold_list)
    payout_table(money_credit)
    for card in hand:
        print(card["face"], end=" ")
    print("\n")
    # print(hand_evaluate(hand))

    while True:
        print("\n")
        new_hand = hold(hand, deck)
        print("\n")
        os.system("clear")
        intro()
        res = hand_evaluate(new_hand)
        new_credit = credit(res, money_credit)
        payout_table(new_credit)
        for card in new_hand:
            print(card["face"], end=" ")
        print("\n")
        print(hand_evaluate(new_hand))


if __name__ == "__main__":
    main()
