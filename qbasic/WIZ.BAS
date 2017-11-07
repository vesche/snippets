MENU:
CLS
GOTO 7
'Game Menu
PRINT "ษออออออออออออออออออออป"
PRINT "บ     Wiz v0.5       บ"
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
PRINT "  = Player (You)"
COLOR 5
LOCATE 5, 1
PRINT "X"
COLOR 7
PRINT "Player becomes visible after your first move."
PRINT
PRINT "Controls:"
PRINT "U: Move player Up"
PRINT "D: Move player Down"
PRINT "R: Move player Right"
PRINT "L: Move player Left"
PRINT "C: Collect Item (While Standing Over)"
PRINT "E: Exit Game"
PRINT
PRINT "Map:"
PRINT "  = Opening (Stand Over to Enter Area)"
PRINT "  = Item (Stand Over Pressing C Collects)"
COLOR 3
LOCATE 17, 1
PRINT "*"
COLOR 2
LOCATE 18, 1
PRINT "I"
COLOR 7
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
LET R% = 5        'Row #
LET c% = 16       'Colloum #
LET H% = 100      'HP Value
LET V% = 0        'Vists to W.House
LET A% = 0        'Vists to R.Hole
LET A$ = " "      'Items

'INPUT
A:
COLOR 4
LOCATE 4, 40
PRINT "ษออออออออออออออออออป"
LOCATE 5, 40
PRINT "บ  Wizard's House  บ"
LOCATE 6, 40
PRINT "บ     ษอออป        บ"
LOCATE 7, 40
PRINT "บ     บ   บ        บ"
LOCATE 8, 40
PRINT "ศอออออผ   ศออออออออผ"
COLOR 3
LOCATE 8, 48
PRINT "*"
COLOR 2
IF A$ = " " THEN
LOCATE 12, 30
PRINT "I"
END IF
COLOR 7
LOCATE 17, 1
PRINT "ษอออออออออออออออออป"
PRINT "บ Legend:         บ"
PRINT "บ   = Opening     บ"
PRINT "บ   = Item        บ"
COLOR 3
LOCATE 19, 3
PRINT "*"
COLOR 2
LOCATE 20, 3
PRINT "I"
COLOR 7
LOCATE 22, 1
PRINT "HP:"; H%
PRINT "Items:"; A$
LOCATE 21, 1
PRINT "ศอออออออออออออออออฮออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออ"
LOCATE 22, 19
PRINT "บ"
LOCATE 23, 19
PRINT "บ"
LOCATE 24, 19
PRINT "บ"
LOCATE 22, 20
PRINT "WEST: SWAMPS, EAST: CASTLE"
LOCATE R%, c%
COLOR 5
PRINT "X"
COLOR 7
b:
LOCATE 21, 20
INPUT "> ", I$
I$ = UCASE$(I$)
SELECT CASE I$

CASE IS = "C"
IF R% = 11 AND c% = 30 THEN
A$ = "CLOAK"
CLS
GOTO A
END IF
CLS
GOTO A

'Down Case
CASE IS = "D"
IF R% = 6 AND c% = 48 AND V% > 0 THEN
GOTO DEAD
END IF
IF R% = 6 AND c% = 48 AND V% < 1 THEN
CLS
GOTO 5
END IF
CLS
LET R% = R% + 1
GOTO A

'Up Case
CASE IS = "U"
IF R% < 2 THEN
CLS
LET R% = R%
GOTO A
END IF
IF R% = 8 AND c% = 48 AND V% > 0 THEN
GOTO DEAD
END IF
IF R% = 8 AND c% = 48 AND V% < 1 THEN
CLS
GOTO 5
END IF
CLS
LET R% = R% - 1
GOTO A


'Right Case
CASE IS = "R"
IF R% = 7 AND c% = 47 AND V% > 0 THEN
GOTO DEAD
END IF
IF R% = 7 AND c% = 47 AND V% < 1 THEN
CLS
GOTO 5
END IF
CLS
LET c% = c% + 1
GOTO A

'Left Case
CASE IS = "L"
IF c% < 2 THEN
CLS
GOTO 6
END IF
IF R% = 7 AND c% = 49 AND V% > 0 THEN
GOTO DEAD
END IF
IF R% = 7 AND c% = 49 AND V% < 1 THEN
CLS
GOTO 5
END IF
CLS
LET c% = c% - 1
GOTO A

'Exit Case
CASE IS = "E"
END

CASE ELSE
CLS
GOTO A
END SELECT

CASE ELSE
PRINT
PRINT "Please choose 1, 2 or 3:"
GOTO MENU
END SELECT

'Inside Wizard's House
5 PRINT "INSIDE WIZARDS HOUSE:"
PRINT
PRINT "Wizard: What can I do for ya?"
PRINT "1. Train Me!"
PRINT "2. You smell funny..."
INPUT2:
INPUT "> ", Y$
SELECT CASE Y$
CASE IS = "2"
PRINT
PRINT "The Wizard's eyes burn red and you fall to the floor lifless."
H% = H% - 100
PRINT
PRINT "GAME OVER"
PRINT "Press Return to go back to the Main Menu."
INPUT "> ", x$
GOTO MENU

'Wizard Training
CASE IS = "1"
CLS
PRINT "Wizard: I think it is time that I pass my powers on to you... All the training  you need is that when you recive my powers whatever you can think can happen"
PRINT "with enough will power."
PRINT
PRINT "The Wizards eyes glow blue and he slowly staggers forward and puts a hand on"
PRINT "your forehead."
PRINT "The Wizard cripples and falls."
PRINT "All the sudden you black out..."
PRINT
PRINT "Press Return to Continue."
INPUT "> ", T$
CLS
PRINT "You awake, and feel powerful."
PRINT "The Wizard lies lifeless next to you."
PRINT
PRINT "Press Return to Continue."
INPUT "> ", R$
DEAD:
CLS
PRINT "Bloody Mess..."
PRINT
PRINT "Should you:"
PRINT "1. Leave at Once"
PRINT "2. Carry the Old Hermit to the Graveyard"
PRINT "3. Search the Wizard's House"
INPUT3:
INPUT "> ", S$
SELECT CASE S$
CASE IS = "1"
CLS
V% = V% + 1
GOTO A
CASE IS = "2"
PRINT
PRINT "Heck No! You can hardly drag the fat lubbox, much less carry him."
GOTO INPUT3
CASE IS = "3"
PRINT
PRINT "Not much to see here, just an old dead dude."
GOTO INPUT3
CASE ELSE
PRINT
PRINT "Please choose 1, 2, or 3:"
GOTO INPUT3
END SELECT

6
LET R% = 8
LET c% = 78

'rabbit hole map set up
CLS
c:
COLOR 6
LOCATE 10, 1
PRINT "ษอออออออออออออออป"
PRINT "บ Rabbit's Hole บ ( )"
PRINT "ศอออออออออออออออผ"
COLOR 3
LOCATE 11, 20
PRINT "*"
COLOR 7
LOCATE 17, 1
PRINT "ษอออออออออออออออออป"
PRINT "บ Legend:         บ"
PRINT "บ   = Opening     บ"
PRINT "บ   = Item        บ"
COLOR 3
LOCATE 19, 3
PRINT "*"
COLOR 2
LOCATE 20, 3
PRINT "I"
COLOR 7
LOCATE 22, 1
PRINT "HP:"; H%
PRINT "Items:"; A$
LOCATE 21, 1
PRINT "ศอออออออออออออออออฮออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออ"
LOCATE 22, 19
PRINT "บ"
LOCATE 23, 19
PRINT "บ"
LOCATE 24, 19
PRINT "บ"
LOCATE R%, c%
COLOR 5
PRINT "X"
D:
COLOR 7
LOCATE 21, 20
INPUT "> ", I$
I$ = UCASE$(I$)
SELECT CASE I$


'Down Case
CASE IS = "D"
IF R% = 10 AND c% = 20 THEN
CLS
GOTO 7
END IF
CLS
LET R% = R% + 1
GOTO c

'Up Case
CASE IS = "U"
IF R% = 12 AND c% = 20 THEN
CLS
GOTO 7
END IF
CLS
LET R% = R% - 1
GOTO c

'Right Case
CASE IS = "R"
IF R% = 11 AND c% = 19 THEN
CLS
GOTO 7
END IF
CLS
LET c% = c% + 1
GOTO c

'Left Case
CASE IS = "L"
IF R% = 11 AND c% = 21 THEN
CLS
GOTO 7
END IF
CLS
LET c% = c% - 1
GOTO c

'Exit Case
CASE IS = "E"
END

CASE ELSE
GOTO D
END SELECT








CASE ELSE
PRINT
PRINT "Please choose 1, 2, or 3:"
GOTO INPUT2
END SELECT


7 CLS
PRINT "INSIDE RABBIT'S HOLE"
PRINT
PRINT "Riddle Rabbit: I will give you a riddle, answer it correctly and I will grant you with my special treasure."
PRINT
PRINT "Press Enter to Continue."
INPUT "> ", L2$
CLS
PRINT "Riddle Rabbit: (Type x to exit. You can guess as many times as you like.)"
PRINT
8 PRINT "What goes around the world but always stays in a corner?"
PRINT "Answer with no puncuation and don't add a, an, or the to your answer."
INPUT "> ", L3$
L3$ = UCASE$(L3$)
SELECT CASE L3$
CASE IS = "x"
CLS
GOTO c
CASE IS = "stamp"
PRINT
PRINT "CORRECT! Amazing!"
CASE ELSE
PRINT "Sorry thats not correct, guess again.."
PRINT
GOTO 8

END SELECT






