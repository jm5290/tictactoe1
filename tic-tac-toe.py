board = [
    ['*','*','*'],
    ['*','*','*'],
    ['*','*','*']
]


            


owon=False
xwon=False
#function to displayboard
def board_display(board):
    for row in board:
        for element in row:
            print(element, end="\t") 
        print()
ctr = 0


#function to check win condition for player 1(x)
def xwin(board): 
    global xwon
    for i in range(0,3):
        if board[0][i]=='x' and board[1][i]=='x' and board[2][i]=='x':
            print('Player one (x) wins by vertical.')
            xwon=True
            break
        if board[0][0]=='x' and board [1][1]=='x' and board[2][2]=='x':
            print('Player one (x) wins by diagonal.')
            xwon=True
            break
        if board[2][0]=='x' and board [1][1]=='x' and board[0][2]=='x':
            print('Player one (x) wins by diagonal.')
            xwon=True
            break
        elif board[i][0]=='x' and board[i][1]=='x' and board[i][2]=='x':
            print('Player one (x) wins by horizontal. ')
            xwon=True
            break
   
#function to check win condition for player 2(o)
def owin(board):
    for x in range(0,3):
        global owon
        if board[0][x]=='o' and board[1][x]=='o' and board[2][x]=='o':
            print('Player two (o) wins by vertical.')
            owon=True
            break
        if board[0][0]=='o' and board [1][1]=='o' and board[2][2]=='o':
            print('Player two (o) wins by diagonal.')
            owon=True
            break
        if board[2][0]=='o' and board [1][1]=='o' and board[0][2]=='o':
            print('Player two (o) wins by diagonal.')
            owon=True
            break
        elif board[x][0]=='o' and board[x][1]=='o' and board[x][2]=='o':
            print('Player two (o) wins by horizontal. ')
            owon=True
            break
 

#gameplay
print('Play your turn by entering where on the grid you would like to play:\n')
print("Do not play in an occupied spot. Free spaces are detonated by an asterix '*'\n ")
print("Choose row/column placement by numbers 0,1,2 in chronological order.\n")
print('Begin:\n')

board_display(board)
print('\n')


while owon==False and xwon==False :
    rx =int(input("Player 1(x) enter row placement: "))
    cx= int(input("Player 1(x) enter column placement: "))
    #validation check to see if spot is availible for x

    while board[rx][cx]!='*':
        print('Space not availible. Try again.\n')
        rx =int(input("Player 1(x) enter row placement: "))
        cx= int(input("Player 1(x) enter column placement: "))

    ctr=ctr+1

    board[rx][cx]= 'x'
    board_display(board)
    print('\n')
    xwin(board)
    owin(board)

    if ctr == 9:
        if owon==False and xwon==False:
            print('Game is a draw. Neither player has won. Displaying final board:')
            board_display(board)
            break ; 

    if(owon or xwon):
        break ; 

    #validation check to see if spot is availible for x
    ro= int(input("Player 2(o) enter row placement: "))
    co= int(input("Player 2(o) enter column placement: "))

    while board[ro][co]!='*':
        print('Space not availible. Try again.\n')
        ro =int(input("Player 2(0) enter row placement: "))
        co =int(input("Player 2(0) enter column placement: "))

    
    ctr=ctr+1

    board[ro][co]= 'o'
    board_display(board)
    print('\n')
    xwin(board)
    owin(board) 
    if ctr == 9:
        if owon==False and xwon==False:
            print('Game is a draw. Neither team has won. Displaying final board:')
            board_display(board)
            print('\n')
            break ; 
    
        if(owon or xwon):
            break ; 
    