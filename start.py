string = input('Enter your Secret word: ')

print('This word has {} letters'.format(len(string)))
s = input('Enter your letter: ')
word =' '.join(s)

def ask_let(s):
    #while s in string:
    if s in string:
        print('You guess the letter number {} '.format(string.index(s)+1))
        #return s
        #word.append(s)
        print('Your answer is ', word)
    else:
        print('No such letter in this word')
        #return s

def only_lett(string):
    for letter in string:
        if letter not in "abcdefghijklmnopqrstuvwxyz":
            print("Wrong input")
    return True

ask_let(s)
