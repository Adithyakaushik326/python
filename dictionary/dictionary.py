import json
from difflib import get_close_matches as gcm
data = json.load(open("data.json",'r'))
def return_definition(word):

    word = word.lower()
    error_tolerance = 0.7
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(gcm(word,data.keys(),cutoff = error_tolerance))!=0:
        reply = input("Did u mean {0}?Enter the index or enter N.".format(gcm(word,data.keys(),cutoff = error_tolerance)))
        if reply == '1':
            return data[gcm(word,data.keys(),cutoff = error_tolerance)[0]]
        elif reply =="2":
            return data[gcm(word,data.keys(),cutoff = error_tolerance)[1]]
        elif reply == "3":
            return data[gcm(word,data.keys(),cutoff = error_tolerance)[2]]
        elif reply == 'N':
            return "The word doesn't exist. PLease check again."
        else:
            return "Didn't understand your entry."
    else:
        return ["The word doesn't exist. Please check again."]

word = input("Enter a Word to search in the Dictionary: ")

definitions = return_definition(word)

if type(definitions) == list:
    for item in definitions:
        print(item)
else:
    print(definitions)
