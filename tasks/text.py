from typing import Optional

__all__ = (
    'find_shortest_longest_word',
)


def find_shortest_longest_word(text: str) -> tuple[Optional[str], Optional[str]]:
    """
    В переданном тексте вернуть слово имеющее наименьшую и наибольшую длину.
    Если такого слова нет - вернуть None
    """
    mini, maxi = None, None
    word = ''
    for i in range(len(text)):
        if text[i].isalnum():
            word += text[i]
        elif not text[i].isalnum():
            if (maxi == None or len(word) > len(maxi)) and len(word) != 0:
                maxi = word
            if (mini == None or len(word) < len(mini)) and len(word) != 0:
                mini = word
            word = ''

    if (maxi == None or len(word) > len(maxi)) and len(word) != 0:
        maxi = word
    if (mini == None or len(word) < len(mini)) and len(word) != 0:
        mini = word
    return (mini, maxi)
