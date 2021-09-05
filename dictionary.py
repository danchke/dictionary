import json
from difflib import SequenceMatcher
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif w.title() in data:
        return data[w.title()]
    elif w.upper() in data:
        return data[w.upper()]
    elif len(get_close_matches(w, data.keys())) > 0:
        yn = input("Did you mean %s instead? Enter Y if yes or N is no." % get_close_matches(w, data.keys())[0])
        yn = yn.upper()
        if yn == "Y":
            return data[get_close_matches(w, data.keys())[0]]
        elif yn == "N":
            return "This word does not exist. Please try again."
        else:
            return "We didn't understand your entry."
    else:
        return "The word doesn't exist. Please check it."

word = input("Enter word: ")

output = translate(word)

if type(output) == list:
    for i in output:
        print(i)
else:
    print(output)

