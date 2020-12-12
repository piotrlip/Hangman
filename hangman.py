from random import choice

print('H A N G M A N')

while True:
    print('Type "play" to play the game, "exit" to quit: ')
    if str(input()) == 'play':
        break
    elif str(input()) == 'exit':
        exit()
words_list = ['python', 'java', 'kotlin', 'javascript']  # 'python', 'java', 'kotlin',
word = list(choice(words_list))
game_board = list('-' * len(word))
# print(''.join(game_board))
count_tries = 7
used_letters = []

while True:
    print()
    print(''.join(game_board))
    move = str(input("Input a letter:"))
    if len(move) != 1:
        print('You should input a single letter')
        continue
    elif not move.islower():
        print('Please enter a lowercase English letter')
        continue
    if move in used_letters:
        if used_letters.count(move) >= 1:
            print("You've already guessed this letter")
        used_letters.append(move)
        continue
    elif move not in word:
        if word == game_board and count_tries >= 0:
            print('You guessed the word ' + str(word) + '!')
            print('You survived!')
            break
        elif word != game_board and count_tries == 0:
            print("That letter doesn't appear in the word")
            print('You lost!')
            break
        print("That letter doesn't appear in the word")
        # print(''.join(game_board))
        count_tries -= 1
        used_letters.append(move)
        continue
    elif move in word:
        letter_index = word.index(move)
        game_board[letter_index] = move
        used_letters.append(move)
        if word == game_board and count_tries >= 0:
            print('You guessed the word ' + str(word) + '!')
            print('You survived!')
            break
        elif word != game_board and count_tries == 0 and used_letters.count(move) >= 2:
            print("You've already guessed this letter")
            print('You lost!')
            break
        elif word != game_board and count_tries == 0:
            print("That letter doesn't appear in the word")
            print('You lost!')
            break
        continue
