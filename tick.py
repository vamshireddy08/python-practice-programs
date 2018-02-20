def print_board(board):
    print '   |   |   '    
    print ' ' + str(board[0])+' | '+str(board[1])+' | '+str(board[2])
    print '   |   |   '
    print '-----------'
    print '   |   |   '    
    print ' ' + str(board[3])+' | '+str(board[4])+' | '+str(board[5])
    print '   |   |   '
    print '-----------'
    print '   |   |   '    
    print ' ' + str(board[6])+' | '+str(board[7])+' | '+str(board[8])
    print '   |   |   '

def checkcode(info):
    if info[0]=='o' or info[0]=='x':
        if info[1]=='o' and info[2]=='o' and info[0]=='o':
            return 2 
        elif info[1]=='x' and info[2]=='x'and info[0]=='x':
            return 1
        if info[3]=='o' and info[6]=='o' and info[0]=='o':
            return 2
        elif info[3]=='x' and info[6]=='x' and info[0]=='x':
            return 1
        if info[4]=='o' and info[8]=='o' and info[0]=='o':
            return 2
        elif info[4]=='x' and info[8]=='x' and info[0]=='x':
            return 1

    if info[8]=='o' or info[8]=='x':
        if info[5]=='o' and info[2]=='o' and info[8]=='o':
            return 2
        elif info[5]=='x' and info[2]=='x' and info[8]=='x':
            return 1
        if info[7]=='o' and info[6]=='o' and info[8]=='o':
            return 2
        elif info[7]=='x' and info[6]=='x' and info[8]=='x':
            return 1
    if info[4]=='o' or info[4]=='x':
        if info[1]=='o' and info[7]=='o' and info[4]=='o':
            return 2
        elif info[1]=='x' and info[7]=='x' and info[4]=='x':
            return 1
        if info[3]=='o' and info[5]=='o' and info[4]=='o':
            return 2
        elif info[3]=='x' and info[5]=='x' and info[4]=='x':
            return 1
        if info[2]=='o' and info[6]=='o' and info[4]=='o':
            return 2
        elif info[2]=='x' and info[6]=='x' and info[4]=='x':
            return 1

def start_game(  ):
    i=0
    turn=True
    won=0
    found=0
    
    record_position=[]
    board=[' ',' ',' ',' ',' ',' ',' ',' ',' ']
    while i<9:
    
        if turn==True:
            user_input=raw_input("player 1 turn ")        
        else:
            user_input=raw_input("player 2 turn ")
        
        for x in range(0,len(record_position),1):
            if record_position[x]==user_input:
                found=1
    
        record_position.append(user_input)
        if found==0:         
            if i%2==0:
                board[int(user_input)]='x'    
            else:
                board[int(user_input)]='o'
            i=i+1
            turn= not turn
          
        else:
            found=0
        print_board(board)

        if i>3:
            won=checkcode(board)
            if(won==1):
                print "player 1 won"
               # quit()                
                break 
            if(won==2):
                print "player 2 won"
               # quit()
                break
    if i==9 and checkcode(board)!=1 and checkcode(board)!=2:
        print "the game is tied\n"

while True:
    
    intrest=input(" welcome to Tic Tack Toe game  \n  press 1 to play\n   press any other key to exit\n")
    if intrest==1:
        start_game()
    else:
        quit()
