vovels = 'aeiouy'

def pig_Latin():
    word = input('Type a word for its pig Latin translation: ')    
    if word[0] in vovels :
        print(word + 'way')
    else:
        print(word[1:] + word[0] + 'ay')

    try_again = input('\n\nTry again? (Press Enter or type n to stop)\n ')
    if try_again == 'n':
        quit()
    else :
        pig_Latin()

pig_Latin()
