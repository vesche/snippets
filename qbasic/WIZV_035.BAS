MENU:
CLS

'Game Menu
PRINT "ษออออออออออออออออออออป"
PRINT "บ     Wiz v0.35      บ"
PRINT "บ By: Austin Jackson บ"
PRINT "ศออออออออออออออออออออผ"
PRINT
PRINT "Select Option:"
PRINT "1. Start Game"
PRINT "2. How to Play"
PRINT "3. Exit"
INPUT "> ", M$
SELECT CASE M$

'How to Play
CASE IS = "2"
CLS
PRINT "ษอออออออออออออป"
PRINT "บ How to Play บ"
PRINT "ศอออออออออออออผ"
PRINT
PRINT "X = Player (You)"
PRINT "Player becomes visible after your first move."
PRINT
PRINT "Controls:"
PRINT "U: Move player Up"
PRINT "D: Move player Down"
PRINT "R: Move player Right"
PRINT "L: Move player Left"
PRINT "E: Exit Game"
PRINT
PRINT "Press return to go back to the Main Menu."
INPUT "> ", Z$
GOTO MENU

'Exit
CASE IS = "3"
END

'Game Start
CASE IS = "1"
CLS

'Character
LET R% = 1
LET C% = 1

'INPUT
a:
LOCATE 2, 40
PRINT "    ___________________"
LOCATE 3, 40
PRINT "   /                  /"
LOCATE 4, 40
PRINT " /__________________/ |"
LOCATE 5, 40
PRINT "|  Wizard's House  |  |"
LOCATE 6, 40
PRINT "|      ___         |  |"
LOCATE 7, 40
PRINT "|     |   |        |  /"
LOCATE 8, 40
PRINT "|_____|___|________|/ "
LOCATE
LOCATE 22, 1
PRINT "Wiz v0.35"
PRINT "X = PLAYER"
LOCATE 21, 1
PRINT "________________________________________________________________________________"
LOCATE 22, 19
PRINT "|"
LOCATE 23, 19
PRINT "|"
LOCATE 24, 19
PRINT "|"
LOCATE 21, 20
PRINT "INPUT (U = UP, D = DOWN, R = RIGHT, L = LEFT, E = EXIT):"
b:
LOCATE 22, 20
INPUT "> ", I$
I$ = UCASE$(I$)
SELECT CASE I$

'Down Case
CASE IS = "D"
CLS
LET R% = R% + 1
LOCATE R%, C%
PRINT "X"
GOTO a

'Up Case
CASE IS = "U"
CLS
LET R% = R% - 1
LOCATE R%, C%
PRINT "X"
GOTO a

'Right Case
CASE IS = "R"
CLS
LET C% = C% + 1
LOCATE R%, C%
PRINT "X"
GOTO a

'Left Case
CASE IS = "L"
CLS
LET C% = C% - 1
LOCATE R%, C%
PRINT "X"
GOTO a

'Exit Case
CASE IS = "E"
END

CASE ELSE
GOTO b
END SELECT

CASE ELSE
PRINT
PRINT "Please choose 1, 2 or 3:"
GOTO MENU
END SELECT





