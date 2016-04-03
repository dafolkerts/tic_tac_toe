
spaces = ['1','2','3','4','5','6','7','8','9']
#open_spaces = ['1','2','3','4','5','6','7','8','9']

def player_1(spaces):   # Playing O's
	play = input('Player 1, what square will you play?:  ')
	for i,j in enumerate(spaces):
		if play == j:
			spaces[i] = 'O'
	return spaces

def player_2(spaces):   # Playing X's
	play = input('Player 2, what square will you play?:  ')
	for i,j in enumerate(spaces):
		if play == j:
			spaces[i] = 'X'
	return spaces

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

for x in range(4):
	spaces = player_1(spaces)
	print_board(spaces)
	if someone_won(spaces):
		print('Player 1 wins!')
		break
	spaces = player_2(spaces)
	print_board(spaces)
	if someone_won(spaces):
		print('Player 2 wins!')
		break

print('It\'s a tie!')

