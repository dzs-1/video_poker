import random


def card_generator():
    s_a = "🂡"
    s_2 = "🂢"
    s_3 = "🂣"
    s_4 = "🂤"
    s_5 = "🂥"
    s_6 = "🂦"
    s_7 = "🂧"
    s_8 = "🂨"
    s_9 = "🂩"
    s_10 = "🂪"
    s_j = "🂫"
    s_q = "🂭"
    s_k = "🂮"

    h_a = "🂱"
    h_2 = "🂲"
    h_3 = "🂳"
    h_4 = "🂴"
    h_5 = "🂵"
    h_6 = "🂶"
    h_7 = "🂷"
    h_8 = "🂸"
    h_9 = "🂹"
    h_10 = "🂺"
    h_j = "🂻"
    h_q = "🂽"
    h_k = "🂾"

    d_a = "🃁"
    d_2 = "🃂"
    d_3 = "🃃"
    d_4 = "🃄"
    d_5 = "🃅"
    d_6 = "🃆"
    d_7 = "🃇"
    d_8 = "🃈"
    d_9 = "🃉"
    d_10 = "🃊"
    d_j = "🃋"
    d_q = "🃍"
    d_k = "🃎"

    c_a = "🃑"
    c_2 = "🃒"
    c_3 = "🃓"
    c_4 = "🃔"
    c_5 = "🃕"
    c_6 = "🃖"
    c_7 = "🃗"
    c_8 = "🃘"
    c_9 = "🃙"
    c_10 = "🃚"
    c_j = "🃛"
    c_q = "🃝"
    c_k = "🃞"

    cards = [s_a, s_2, s_3, s_4, s_5, s_6, s_7, s_8, s_9, s_10, s_j, s_q, s_k,
             h_a, h_2, h_3, h_4, h_5, h_6, h_7, h_8, h_9, h_10, h_j, h_q, h_k,
             d_a, d_2, d_3, d_4, d_5, d_6, d_7, d_8, d_9, d_10, d_j, d_q, d_k,
             c_a, c_2, c_3, c_4, c_5, c_6, c_7, c_8, c_9, c_10, c_j, c_q, c_k]

    return cards


# def hand_check(hand):
#     for card in hand:


def deal(cards):
    dealt_cards = []
    for i in range(5):
        dealt_cards.append(random.choice(cards))
    return dealt_cards


def main():
    cards = card_generator()
    print(" ".join(deal(cards)))


if __name__ == "__main__":
    main()
