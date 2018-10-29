import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(word):
    word = word.lower()
    if (word in data.keys()):
        return data[word]
    elif (word.title() in data.keys()):
        return data[word.title()]
    elif (word.upper() in data):
        return data[word.upper()]
    elif (len(get_close_matches(word, data.keys())) > 0):
        yn = input("Did you mean %s instead? Enter Y is yes, or N if no." % get_close_matches(word, data.keys())[0].upper())
        if yn.upper() == "Y":
            return data[get_close_matches(word, data.keys())[0]]
        elif yn.upper() == "N":
            return "The word does not exist."
        else:
            return "Invalid input"
    else:
        return "The word does not exist."
word = input("Enter word: ")

output = translate(word)
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
