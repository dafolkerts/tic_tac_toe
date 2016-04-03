import random

spaces = ['1','2','3','4','5','6','7','8','9']
open_spaces = ['1','2','3','4','5','6','7','8','9']

def player_1(spaces, open_spaces):   # Human - Playing O's
	play = input('Human, what square will you play?:  ')
	for i,j in enumerate(spaces):
		if play == j:
			spaces[i] = 'O'
	open_spaces.remove(play)
	return spaces, open_spaces

def player_2(spaces, open_spaces):   # Computer - Playing X's randomly
	if len(open_spaces) == 0:
		return spaces, open_spaces
	print('The computer plays: ')
	play = open_spaces[random.randint(0,(len(open_spaces)-1))]
	for i,j in enumerate(spaces):
		if play == j:
			spaces[i] = 'X'
	open_spaces.remove(play)
	return spaces, open_spaces

def print_board(spaces):
	board = """
	 {} | {} | {} 
	-----------
	 {} | {} | {} 
	-----------
	 {} | {} | {} 
	""".format(spaces[0], spaces[1], spaces[2], spaces[3], \
	spaces[4], spaces[5], spaces[6], spaces[7], spaces[8])
	print(board)

def someone_won(spaces):
	if spaces[0] == spaces[1] == spaces[2]:
		return True
	elif spaces[3] == spaces[4] == spaces[5]:
		return True
	elif spaces[6] == spaces[7] == spaces[8]:
		return True
	elif spaces[0] == spaces[3] == spaces[6]:
		return True
	elif spaces[1] == spaces[4] == spaces[7]:
		return True
	elif spaces[2] == spaces[5] == spaces[8]:
		return True
	elif spaces[0] == spaces[4] == spaces[8]:
		return True
	elif spaces[6] == spaces[4] == spaces[2]:
		return True
	else:
		return False

print_board(spaces)

for x in range(5):
	spaces, open_spaces = player_1(spaces, open_spaces)
	print_board(spaces)
	if someone_won(spaces):
		print('The human wins!')
		break
	spaces, open_spaces = player_2(spaces, open_spaces)
	print_board(spaces)
	if someone_won(spaces):
		print('The computer wins!')
		break

if someone_won(spaces) == False:
	print('It\'s a tie!')

