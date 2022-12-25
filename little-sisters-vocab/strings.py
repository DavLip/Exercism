"""Functions for creating, transforming, and adding prefixes to strings."""


def add_prefix_un(word):
    """Take the given word and add the 'un' prefix.

    :param word: str - containing the root word.
    :return: str - of root word prepended with 'un'.
    """

    return ''.join(['un', word])



def make_word_groups(vocab_words):
    """Transform a list containing a prefix and words into a string with the prefix followed by the words with prefix prepended.

    :param vocab_words: list - of vocabulary words with prefix in first index.
    :return: str - of prefix followed by vocabulary words with
            prefix applied.

    This function takes a `vocab_words` list and returns a string
    with the prefix and the words with prefix applied, separated
     by ' :: '.

    For example: list('en', 'close', 'joy', 'lighten'),
    produces the following string: 'en :: enclose :: enjoy :: enlighten'.
    """

    sliced_list = vocab_words[1:]
    prefix = vocab_words[0] #auto
    final_list = []
    final_list.append(prefix)
    for word in sliced_list:
        prefix_list = []
        prefix_list.append(prefix) #['auto']
        temp_prefix = prefix_list
        temp_prefix.append(word) #['auto', 'didactic']
        join_list = ''.join(temp_prefix) #'autodidactic'
        final_list.append(join_list)

    return ' :: '.join(final_list)


def remove_suffix_ness(word):
    """Remove the suffix from the word while keeping spelling in mind.

    :param word: str - of word to remove suffix from.
    :return: str - of word with suffix removed & spelling adjusted.

    For example: "heaviness" becomes "heavy", but "sadness" becomes "sad".
    """
    suffix_removed = word[:-4]
    if suffix_removed[-1] == 'i':
        return suffix_removed[:-1] + 'y'
    return suffix_removed


def adjective_to_verb(sentence, index):
    """Change the adjective within the sentence to a verb.

    :param sentence: str - that uses the word in sentence.
    :param index: int - index of the word to remove and transform.
    :return: str - word that changes the extracted adjective to a verb.

    For example, ("It got dark as the sun set", 2) becomes "darken".
    """

    split_sentence = sentence.split()
    adjective = split_sentence[index]
    if adjective[-1] == '.':
        return adjective[:-1] + 'en'
    return adjective + 'en'
