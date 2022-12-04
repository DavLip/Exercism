"""Functions to help play and score a game of blackjack.

How to play blackjack:    https://bicyclecards.com/how-to-play/blackjack/
"Standard" playing cards: https://en.wikipedia.org/wiki/Standard_52-card_deck
"""


def value_of_card(card):
    """Determine the scoring value of a card.

    :param card: str - given card.
    :return: int - value of a given card.  See below for values.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 1
    3.  '2' - '10' = numerical value.
    """

    num_range = []
    for num in range(2, 11, 1):
        num_str = str(num)
        num_range.append(num_str)

    if card in ('J', 'Q', 'K'):
        return 10
    elif card == 'A':
        return 1
    elif card in num_range:
        return int(card)


def higher_card(card_one, card_two):
    """Determine which card has a higher value in the hand.

    :param card_one, card_two: str - cards dealt in hand.  See below for values.
    :return: str or tuple - resulting Tuple contains both cards if they are of equal value.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 1
    3.  '2' - '10' = numerical value.
    """

    num_range = []
    for num in range(2, 11, 1):
        num_str = str(num)
        num_range.append(num_str)

    if card_one in ('J', 'Q', 'K'):
        card_one_num = 10
    elif card_one == 'A':
        card_one_num = 1
    elif card_one in num_range:
        card_one_num = int(card_one)

    if card_two in ('J', 'Q', 'K'):
        card_two_num = 10
    elif card_two == 'A':
        card_two_num = 1
    elif card_two in num_range:
        card_two_num = int(card_two)

    if card_one_num > card_two_num:
        return card_one
    elif card_two_num > card_one_num:
        return card_two
    else:
        return (card_one, card_two)


def value_of_ace(card_one, card_two):
    """Calculate the most advantageous value for the ace card.

    :param card_one, card_two: str - card dealt. See below for values.
    :return: int - either 1 or 11 value of the upcoming ace card.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 11 (if already in hand)
    3.  '2' - '10' = numerical value.
    """

    num_range = []
    for num in range(2, 11, 1):
        num_str = str(num)
        num_range.append(num_str)

    if card_one in ('J', 'Q', 'K'):
        card_one = 10
    elif card_one == 'A':
        card_one = 11
    elif card_one in num_range:
        card_one = int(card_one)

    if card_two in ('J', 'Q', 'K'):
        card_two = 10
    elif card_two == 'A':
        card_two = 11
    elif card_two in num_range:
        card_two = int(card_two)

    if 21 - (card_one + card_two) >= 11:
        return 11
    else:
        return 1

    


def is_blackjack(card_one, card_two):
    """Determine if the hand is a 'natural' or 'blackjack'.

    :param card_one, card_two: str - card dealt. See below for values.
    :return: bool - is the hand is a blackjack (two cards worth 21).

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 11 (if already in hand)
    3.  '2' - '10' = numerical value.
    """

    hand = [card_one, card_two]
    ten_card = ('10', 'J', 'Q', 'K')
    if card_one == card_two:
        return False
    elif hand.count('A') == 1:
        for card in hand:
            if card == 'A':
                continue
            elif card in ten_card:
                return True
            else:
                return False
    else:
        return False


def can_split_pairs(card_one, card_two):
    """Determine if a player can split their hand into two hands.

    :param card_one, card_two: str - cards dealt.
    :return: bool - can the hand be split into two pairs? (i.e. cards are of the same value).
    """

    ten_card = ('10', 'J', 'Q', 'K')
    if card_one == card_two:
        return True
    elif card_one in ten_card and card_two in ten_card:
        return True
    else:
        return False


def can_double_down(card_one, card_two):
    """Determine if a blackjack player can place a double down bet.

    :param card_one, card_two: str - first and second cards in hand.
    :return: bool - can the hand can be doubled down? (i.e. totals 9, 10 or 11 points).
    """

    cards = [card_one, card_two]
    num_range = []
    card_num = 0
    for num in range(2, 11, 1):
        num_str = str(num)
        num_range.append(num_str)

    for card in cards:
        if card in ('J', 'Q', 'K'):
            card = 10
        elif card == 'A':
            card = 1
        elif card in num_range:
            card = int(card)
        
        card_num += card

    if 9 <= card_num <= 11:
        return True
    else:
        return False
