def sort_on(dict):
    return dict["num"]

def count_words(text):
    return len(text.split())

def count_characters(text):
    char_dict = {}
    chars = text.lower()

    for c in list(chars):
        if c in char_dict:
            char_dict[c] = char_dict[c]+1
        else:
            char_dict[c] = 1

    return char_dict

def generate_report(dict):
    dict_list = []
    for i in dict:
        dict_list.append({"char":i, "num":dict[i]})

    dict_list.sort(reverse=True, key=sort_on)

    return dict_list