import random
def display_board(board):
  print(board[7]+'  |  '+board[8]+'  |  '+board[9])
  print('----------')
  print(board[4]+'  |  '+board[5]+'  |  '+board[6])
  print('----------')
  print(board[1]+'  |  '+board[2]+'  |  '+board[3])
def player_input():
  marker=''
  while marker!='X' and marker!='O':
    marker=input("Player 1 please choose 'X' or 'O':").upper()
    if marker=='X':
      return ('X','O')
    else:
      return ('O','X')
def place_marker(board,marker,position):
  if board[position]=='':
    board[position]=marker
  else:
    print("You lose a chance since you placed your marker in position which is already filled!!")
    print("In your chance be carefull and place in some other position")
def win_check(board,mark):
  return (board[1]==board[2]==board[3]==mark)or(board[4]==board[5]==board[6]==mark)or(board[7]==board[8]==board[9]==mark)or(board[7]==board[5]==board[3]==mark)or(board[9]==board[5]==board[1]==mark)or(board[1]==board[4]==board[7]==mark)or(board[8]==board[5]==board[2]==mark)or(board[9]==board[6]==board[3]==mark)
def choose_first():  
  flip=random.randint(0,1)
  if flip==0:
    return 'Player 1'
  else:
    return 'Player 2'
def space_check(board,position):
  return board[position]==''
def full_board_check(board):
  for i in range(1,10):
    if space_check(board,i):
      return False
  return True
def player_choice(board):
  position=0
  while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board,position):
    position=int(input("Choose a Position between 1-9:"))
    return position
def replay():
  choice=input("Play Again ? Enter yes to play no to Exit:")
  return choice=='yes'
print("WELCOME TO TIC TAC TOE GAME!!!")
while True:
  the_board=['']*10
  player1_marker,player2_marker=player_input()
  turn=choose_first()
  print(turn+' Will go First')
  play_game=input('Ready to start the Game? Type y to start n to stop')
  if play_game=='y':
    game_on=True
  else:
    game_on=False
  while game_on:
    if turn == 'Player 1':
      display_board(the_board) #its going to display the board
      position=player_choice(the_board) #player has to choose the position 
      place_marker(the_board,player1_marker,position)
      if win_check(the_board,player1_marker):
        display_board(the_board)
        print('Player 1 you have WON!! Congratulations !!')
        game_on=False
      else:
        if full_board_check(the_board):
          display_board(the_board)
          print('TIE GAME')
          game_on=False
        else:
          turn = 'Player 2'
    else:
      display_board(the_board) #its going to display the board
      position=player_choice(the_board) #player has to choose the position 
      place_marker(the_board,player2_marker,position)
      if win_check(the_board,player2_marker):
        display_board(the_board)
        print('Player 2 you have WON!! Congratulations !!')
        game_on=False
      else:
        if full_board_check(the_board):
          display_board(the_board)
          print('TIE GAME!')
          game_on=False
        else:
          turn = 'Player 1'
  if not replay():
    print("Thanks for Playing the Game! Hope you Enjoyed :)")
    break
      
