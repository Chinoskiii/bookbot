def get_num_words(text):
    string = text.split()
    number = len(string)
    return number

def count_characters(text):
    report = {}

    for characters in text:
        characters = characters.lower()
        if characters in report:
            report [characters] += 1
        elif characters not in report:
            report[characters] = 1

    return report

def sorted_list(dictionary):
    
    assorted_list = list(dictionary.items())
    list_of_dictionaries = []

    for i in assorted_list:
        list_of_dictionaries.append({"char" : i[0], "num" : i[1]})

    list_of_dictionaries.sort(reverse=True, key=sort_on_num)

    return list_of_dictionaries

def sort_on_num(dictionary):
    return dictionary["num"]
        