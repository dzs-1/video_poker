import random


def one_pair():         # Jack or better, returns boolean
    pass


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


def card_generator():           # creates card dictionary
    s_a = {"face": "🂡", "value": 1}
    s_2 = {"face": "🂢", "value": 2}
    s_3 = {"face": "🂣", "value": 3}
    s_4 = {"face": "🂤", "value": 4}
    s_5 = {"face": "🂥", "value": 5}
    s_6 = {"face": "🂦", "value": 6}
    s_7 = {"face": "🂧", "value": 7}
    s_8 = {"face": "🂨", "value": 8}
    s_9 = {"face": "🂩", "value": 9}
    s_10 = {"face": "🂪", "value": 10}
    s_j = {"face": "🂫", "value": 11}
    s_q = {"face": "🂭", "value": 12}
    s_k = {"face": "🂮", "value": 13}

    h_a = {"face": "🂱", "value": 1}
    h_2 = {"face": "🂲", "value": 2}
    h_3 = {"face": "🂳", "value": 3}
    h_4 = {"face": "🂴", "value": 4}
    h_5 = {"face": "🂵", "value": 5}
    h_6 = {"face": "🂶", "value": 6}
    h_7 = {"face": "🂷", "value": 7}
    h_8 = {"face": "🂸", "value": 8}
    h_9 = {"face": "🂹", "value": 9}
    h_10 = {"face": "🂺", "value": 10}
    h_j = {"face": "🂻", "value": 11}
    h_q = {"face": "🂽", "value": 12}
    h_k = {"face": "🂾", "value": 13}

    d_a = {"face": "🃁", "value": 1}
    d_2 = {"face": "🃂", "value": 2}
    d_3 = {"face": "🃃", "value": 3}
    d_4 = {"face": "🃄", "value": 4}
    d_5 = {"face": "🃅", "value": 5}
    d_6 = {"face": "🃆", "value": 6}
    d_7 = {"face": "🃇", "value": 7}
    d_8 = {"face": "🃈", "value": 8}
    d_9 = {"face": "🃉", "value": 9}
    d_10 = {"face": "🃊", "value": 10}
    d_j = {"face": "🃋", "value": 11}
    d_q = {"face": "🃍", "value": 12}
    d_k = {"face": "🃎", "value": 13}

    c_a = {"face": "🃑", "value": 1}
    c_2 = {"face": "🃒", "value": 2}
    c_3 = {"face": "🃓", "value": 3}
    c_4 = {"face": "🃔", "value": 4}
    c_5 = {"face": "🃕", "value": 5}
    c_6 = {"face": "🃖", "value": 6}
    c_7 = {"face": "🃗", "value": 7}
    c_8 = {"face": "🃘", "value": 8}
    c_9 = {"face": "🃙", "value": 9}
    c_10 = {"face": "🃚", "value": 10}
    c_j = {"face": "🃛", "value": 11}
    c_q = {"face": "🃝", "value": 12}
    c_k = {"face": "🃞", "value": 13}

    cards = [s_a, s_2, s_3, s_4, s_5, s_6, s_7, s_8, s_9, s_10, s_j, s_q, s_k,
             h_a, h_2, h_3, h_4, h_5, h_6, h_7, h_8, h_9, h_10, h_j, h_q, h_k,
             d_a, d_2, d_3, d_4, d_5, d_6, d_7, d_8, d_9, d_10, d_j, d_q, d_k,
             c_a, c_2, c_3, c_4, c_5, c_6, c_7, c_8, c_9, c_10, c_j, c_q, c_k]

    return cards


def win_check():            # checks all the winning conditions
    pass


def hold():
    pass


def deal(cards):                # deals 5 unique cards
    dealt_cards = []
    while len(dealt_cards) != 5:
        current_card = random.choice(cards)
        if current_card not in dealt_cards:
            dealt_cards.append(current_card)
    return dealt_cards


def main():
    cards = card_generator()
    hand = deal(cards)
    for card in hand:
        print(card["face"])


if __name__ == "__main__":
    main()
