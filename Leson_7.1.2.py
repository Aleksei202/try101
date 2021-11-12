word = True

while word:
    word_enter = str(input("please enter any word"))
    print(word_enter.upper())
    if word_enter == str('STOP'):
        word = False


