"""Functions for tracking poker hands and assorted card tasks.

Python list documentation: https://docs.python.org/3/tutorial/datastructures.html
"""


def get_rounds(number):
    """Create a list containing the current and next two round numbers.

    :param number: int - current round number.
    :return: list - current round and the two that follow.
    """

    rounds = []
    for i in range(number, number + 3, 1):
        rounds.append(i)
    return rounds


def concatenate_rounds(rounds_1, rounds_2):
    """Concatenate two lists of round numbers.

    :param rounds_1: list - first rounds played.
    :param rounds_2: list - second set of rounds played.
    :return: list - all rounds played.
    """

    return rounds_1 + rounds_2


def list_contains_round(rounds, number):
    """Check if the list of rounds contains the specified number.

    :param rounds: list - rounds played.
    :param number: int - round number.
    :return: bool - was the round played?
    """

    return True if number in rounds else False


def card_average(hand):
    """Calculate and returns the average card value from the list.

    :param hand: list - cards in hand.
    :return: float - average value of the cards in the hand.
    """

    return sum(hand)/len(hand)


def approx_average_is_average(hand):
    """Return if an average is using (first + last index values ) OR ('middle' card) == calculated average.

    :param hand: list - cards in hand.
    :return: bool - does one of the approximate averages equal the `true average`?
    """

    act_avg = sum(hand)/len(hand)
    option_1 = [hand[0], hand[-1]]
    option_1_avg = sum(option_1)/2
    median = hand[int((len(hand) - 1)/2)]

    return True if act_avg == option_1_avg or act_avg == median else False


def average_even_is_average_odd(hand):
    """Return if the (average of even indexed card values) == (average of odd indexed card values).

    :param hand: list - cards in hand.
    :return: bool - are even and odd averages equal?
    """

    even_list = []
    for i in range(0,len(hand),2):
        even_list.append(hand[i])

    odd_list = []
    for i in range(1,len(hand),2):
        odd_list.append(hand[i])

    return True if sum(even_list)/len(even_list) == sum(odd_list)/len(odd_list) else False


def maybe_double_last(hand):
    """Multiply a Jack card value in the last index position by 2.

    :param hand: list - cards in hand.
    :return: list - hand with Jacks (if present) value doubled.
    """

    new_hand = hand[:-1]
    if hand[-1] == 11:
        new_hand.append(11*2)
    else:
        new_hand.append(hand[-1])
    
    return new_hand