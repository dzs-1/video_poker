import random


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
                            print("ONE PAIR")


def two_pair():
    pass


def three_of_a_kind():
    pass


def straight():
    pass


def flush():
    pass


def full_house():
    pass


def four_of_a_kind():
    pass


def straight_flush():
    pass


def royal_flush():
    pass


def cards():           # creates card dictionary
    s_a = {"face": "\033[1;31;49m🂡\033[0m", "value": 1, "color": "spades"}
    s_2 = {"face": "\033[1;31;49m🂢\033[0m", "value": 2, "color": "spades"}
    s_3 = {"face": "\033[1;31;49m🂣\033[0m", "value": 3, "color": "spades"}
    s_4 = {"face": "\033[1;31;49m🂤\033[0m", "value": 4, "color": "spades"}
    s_5 = {"face": "\033[1;31;49m🂥\033[0m", "value": 5, "color": "spades"}
    s_6 = {"face": "\033[1;31;49m🂦\033[0m", "value": 6, "color": "spades"}
    s_7 = {"face": "\033[1;31;49m🂧\033[0m", "value": 7, "color": "spades"}
    s_8 = {"face": "\033[1;31;49m🂨\033[0m", "value": 8, "color": "spades"}
    s_9 = {"face": "\033[1;31;49m🂩\033[0m", "value": 9, "color": "spades"}
    s_10 = {"face": "\033[1;31;49m🂪\033[0m", "value": 10, "color": "spades"}
    s_j = {"face": "\033[1;31;49m🂫\033[0m", "value": 11, "color": "spades"}
    s_q = {"face": "\033[1;31;49m🂭\033[0m", "value": 12, "color": "spades"}
    s_k = {"face": "\033[1;31;49m🂮\033[0m", "value": 13, "color": "spades"}

    h_a = {"face": "\033[1;32;49m🂱\033[0m", "value": 1, "color": "hearts"}
    h_2 = {"face": "\033[1;32;49m🂲\033[0m", "value": 2, "color": "hearts"}
    h_3 = {"face": "\033[1;32;49m🂳\033[0m", "value": 3, "color": "hearts"}
    h_4 = {"face": "\033[1;32;49m🂴\033[0m", "value": 4, "color": "hearts"}
    h_5 = {"face": "\033[1;32;49m🂵\033[0m", "value": 5, "color": "hearts"}
    h_6 = {"face": "\033[1;32;49m🂶\033[0m", "value": 6, "color": "hearts"}
    h_7 = {"face": "\033[1;32;49m🂷\033[0m", "value": 7, "color": "hearts"}
    h_8 = {"face": "\033[1;32;49m🂸\033[0m", "value": 8, "color": "hearts"}
    h_9 = {"face": "\033[1;32;49m🂹\033[0m", "value": 9, "color": "hearts"}
    h_10 = {"face": "\033[1;32;49m🂺\033[0m", "value": 10, "color": "hearts"}
    h_j = {"face": "\033[1;32;49m🂻\033[0m", "value": 11, "color": "hearts"}
    h_q = {"face": "\033[1;32;49m🂽\033[0m", "value": 12, "color": "hearts"}
    h_k = {"face": "\033[1;32;49m🂾\033[0m", "value": 13, "color": "hearts"}

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
    cards_to_hold = str(input("Which card(s) to hold? (1-5): "))
    hold_list = []
    for i in cards_to_hold:
        hold_list.append(int(i))
    for i in range(5):
        j = i + 1
        if j not in hold_list:
            current_card = random.choice(deck)
            if current_card not in hand:
                hand[i] = current_card
    return hand


def deal(deck, hold_list):                # deals 5 unique cards
    dealt_cards = []
    while len(dealt_cards) != 5:
        current_card = random.choice(deck)
        if current_card not in dealt_cards:
            dealt_cards.append(current_card)
    return dealt_cards


def main():
    hold_list = []
    deck = cards()
    hand = deal(deck, hold_list)
    for card in hand:
        print(card["face"], end=" ")
    print("\n")
    one_pair(hand)
    while True:
        new_hand = hold(hand, deck)
        print("\n")
        for card in new_hand:
            print(card["face"], end=" ")
        print("\n")
        one_pair(hand)


if __name__ == "__main__":
    main()
