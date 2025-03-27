def vowel_filter(function):

    def wrapper():
        result = function()
        only_vowels = [char for char in result if char in "aeiouy"]
        return only_vowels
    return wrapper


@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e"]


print(get_letters())
