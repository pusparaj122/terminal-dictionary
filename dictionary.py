import json
from difflib import get_close_matches

data = json.load(open("data.json"))
def dictionary(word):
    #it gets close matches to the variable "word" which is the word that user enters and compare it with the close matches in the data
    #keys. when it gets the close matches it usually gets 3 close matches and the 1st one the the most closet so we did [0] just to get 
    #that most closet match to the word we entered.
    #in this get_close_matches we have get_close_matches(word, what to compare with, n, cutoff)
    #word=word we want to compare or simply word that we entered
    #what to compare = What to compare our word for closest match here we use a dictionary keys to compare with
    #n=number of closest match to get. by defult its n=3, means if we compare "rainn" with data.keys() we get three results like [rain, 
    # main, train]. if we increase n to 4, n=4, we get [rain, main, train, pain] so on and so forth.
    #usually the 1st one is the most closest match so we do [0] in our code to get the most closet match.
    #cutoff=it SequenceMatcher ratio. means it matches the ratio of similarity between the word we entered with the word we want to 
    #compare with. it by defult is 0.6 so if the SequenceMatch between the words is greater than 0.6, we get those as our output.
    #its better to keep cutoff as 0.8 so that we get least words but the best ones.
    #fuck = get_close_matches(word, data.keys(), cutoff=0.8)[0]

    if word in data:
        return data[word]
        
    elif get_close_matches(word, data.keys(), cutoff=0.8):
        yn =  input(f"Did you mean {get_close_matches(word, data.keys(), cutoff=0.8)[0]} instead? Enter Y if yes and N if No.")
        if yn == 'y':
            return data[get_close_matches(word, data.keys(), cutoff=0.8)[0]]
        elif yn == 'n':
            return 'No word'
        else:
            return 'Didn\'t understand your input'
    else:
        return 'No words'


i=1
while i>0:
    word = input('Enter the word').lower()

    output = dictionary(word)

    if type (output) == list:
        for item in output:
            print(item)
    else:       
        print(output)
    
    user = input("Do you want to exit?")
    if user == 'y':
        break
    else:
        continue
    i=i+1
    

