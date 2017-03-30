board = ['-','-','-','-','-','-','-','-','-']
player01Wins = False
player02Wins = False
isGameDraw = False

def GameResult():
    res = -1
    if player01Wins:
        global res
        res = 1
        return res
    elif player02Wins:
        global res
        res = 2
        return res
    elif isGameDraw:
        global res
        res = 0
        return res
    return res

def PrintBoard():
    print "\n\n"
    print "*********Tic Tac Toe*********"
    print "         " + board[0] + " " + board[1] + " " + board[2]
    print "         " + board[3] + " " + board[4] + " " + board[5]
    print "         " + board[6] + " " + board[7] + " " + board[8]
    print "*****************************"

def Player01(cellNo):
    cellNo = cellNo - 1
    if cellNo >= len(board):
        print "No such cell!"
        pass
    else:
        board[cellNo] = 'X'
        PrintBoard()

def Player02(cellNo):
    cellNo = cellNo - 1
    if cellNo >= len(board):
        print "No such cell!"
        pass
    else:
        board[cellNo] = 'O'
        PrintBoard

def Reset():
    print "Resetting Board"
    global board
    global isGameDraw
    global player01Wins
    global player02Wins
    i = 0
    for c in board:
        board[i] = '-'
        i += 1
       # print c
    isGameDraw = False
    player01Wins = False
    player02Wins = False
  #  print board

def CheckResult():
   i = 0
   for b in board:
        global player01Wins
        global player02Wins
        global isGameDraw
        if i == 0 or i == 3 or i == 6:
            if board[i] == board[i+1] == board[i+2] == 'X':
                print "Player1 wins"
                player01Wins = True
                player02Wins = False
                isGameDraw = False
            elif board[i] == board[i+1] == board[i+2] == 'O':
                print "Player2 wins"
                player01Wins = False
                player02Wins = True
                isGameDraw = False
        
        if i == 0 or i == 1 or i == 2:
            if board[i] == board[i+3] == board[i+6] == 'X':
                print "Player1 wins"
                player01Wins = True
                player02Wins = False
                isGameDraw = False
            elif board[i] == board[i+3] == board[i+6] == 'O':
                print "Player2 wins"
                player01Wins = False
                player02Wins = True
                isGameDraw = False
        
        if i == 0:
            if board[i] == board[i+4] == board[i+8] == 'X':
                print "Player1 wins"
                player01Wins = True
                player02Wins = False
                isGameDraw = False
            elif board[i] == board[i+4] == board[i+8] == 'O':
                print "Player2 wins"
                player01Wins = False
                player02Wins = True
                isGameDraw = False
                
        if i == 2:
            if board[i] == board[i+2] == board[i+4] == 'X':
                print "Player1 wins"
                player01Wins = True
                player02Wins = False
                isGameDraw = False
            elif board[i] == board[i+2] == board[i+4] == 'O':
                print "Player2 wins"
                player01Wins = False
                player02Wins = True
                isGameDraw = False
        i = i + 1
   
   counter = 0
   for c in board:
        if c == '-':
            counter += 1
   if counter <= 1:
        print "That's a Draw!"
        isGameDraw = True
        player01Wins = False
        player02Wins = False