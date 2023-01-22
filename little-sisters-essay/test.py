def replace_word_choice(sentence, old_word, new_word):
    """Replace a word in the provided sentence with a new one.

    :param sentence: str - a sentence to replace words in.
    :param old_word: str - word to replace.
    :param new_word: str - replacement word.
    :return: str - input sentence with new words in place of old words.
    """

    replace_sentence = sentence.replace(old_word, new_word)
    print(replace_sentence)


replace_word_choice("Animals are cool.", "cool", "awesome")
