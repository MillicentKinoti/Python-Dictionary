import json
import difflib#compares text
from difflib import get_close_matches

data= json.load(open("json/data.json"))


def translate(word):
    #case sensitivity
    word=word.lower()
    if word in data:
        return data[word]
    #checking the similarities of the word
    elif len(get_close_matches(word, data.keys()))> 0:
        yes_or_no=input("Did you mean %s instead? Enter Y if yes or N if no: " % get_close_matches(word, data.keys())[0])
        if yes_or_no == "Y":
            return data[get_close_matches(word, data.keys())[0]]
        elif yes_or_no == "N":
            return "The word does not exist"
        else:
            return " Invalid choice"
    else:
        return "The word does not exist. Try again"

  
#prompts the user to enter the word they are looking searching for

word=input("Enter the word you want to search: ")


output= translate(word)
#generates string for words with more than one definition
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)


