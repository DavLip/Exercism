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

answer = can_double_down('A', '9')
print(answer)