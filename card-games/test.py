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

    print(even_list)
    print(odd_list)
    return True if sum(even_list)/len(even_list) == sum(odd_list)/len(odd_list) else False

test = average_even_is_average_odd([5,6,8])
print(test)