def sort_on(items):
    return items["num"]

def count_word(file_content):
    words = file_content.split()
    return len(words)

def char_occur(file_content):
    lower_content = file_content.lower()
    char_list = list(lower_content)
    char_count = {}
    for char in char_list:
        if char.isalpha():
            if char not in char_count:
                char_count[char] = 1
            else:            
                char_count[char] += 1 
    return char_count

def sorting_dictionnary(dictionnary):
    dictionnary_list = []
    for char in dictionnary:
        individual_char = {
            "char": char,
            "num" : dictionnary[char]
        }
        dictionnary_list.append(individual_char)
    dictionnary_list.sort(reverse=True, key=sort_on)
    return dictionnary_list