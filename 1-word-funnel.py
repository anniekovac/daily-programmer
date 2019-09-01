# Challenge #366 [Easy] Word funnel 1
def word_funnel(word1, word2):
    """
    Checking if word1 == word2 if one of the letters
    was removed from it. Returns True if so.
    :param word1: str
    :param word2: str
    :return: boolean
    """
    if len(word1) > len(word2) + 1 or len(word1) < len(word2):
        return False
    for i, letter in enumerate(word1):
        new_word = ''.join([lett for idx, lett in enumerate(word1) if idx != i])
        if new_word == word2:
            return True
    return False


# print(word_funnel('annie', 'nnie'))
print(word_funnel('leave', 'eave'))  # true
print(word_funnel("reset", "rest"))  # true
print(word_funnel("dragoon", "dragon"))  # true
print(word_funnel("eave", "leave"))  # false
print(word_funnel("sleet", "lets"))  # false
print(word_funnel("skiff", "ski"))  # false