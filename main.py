import PlayerHelper

isGameOn = True
isPlayer01Turn = True

def StartGame():
    global isPlayer01Turn
    isPlayer01Turn = True
    print "Welcome to Ye Olde Tic Tac Toe!"
    print "\n\nPlayer 1 - X||Player 2 - O"
    PlayerHelper.PrintBoard()
    
def Restart():
    global isGameOn
    res = raw_input("Would you like to play again? y/n: ")
    if res == "y" or res == "Y":
        PlayerHelper.Reset()
        PlayerHelper.PrintBoard()
        StartGame()
    else:
        print "Thank you for playing!"
        isGameOn = False
    
def PlayerTurn(playerNo):
    global isPlayer01Turn
    if playerNo == 1:
        cell = input("Player 1, Enter cell number:")
        if 1 <= cell <= 9:
            PlayerHelper.Player01(cell)
            PlayerHelper.CheckResult()
            isPlayer01Turn = False
        else:
            print "Please Enter numbers between 1 and 9..."
    elif playerNo == 2:
        cell = input("Player 2, Enter cell number:")
        if 1 <= cell <= 9:
            PlayerHelper.Player02(cell)
            PlayerHelper.CheckResult()
            isPlayer01Turn = True
        else:
            print "Please Enter numbers between 1 and 9..."
    
PlayerHelper.Reset()
StartGame()
while isGameOn:
    if isPlayer01Turn:
        PlayerTurn(1)
        if PlayerHelper.GameResult() != -1:
            Restart()
           # break
    else:
        PlayerTurn(2)
        if PlayerHelper.GameResult() != -1:
            Restart()
           # break