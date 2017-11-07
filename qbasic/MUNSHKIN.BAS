0 CLS
PRINT "ÉÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍ»"
PRINT "º  Munshkin : Text Adventure   º"
PRINT "º                              º"
PRINT "º     By: Austin Jackson       º"
PRINT "º                              º"
PRINT "ºOrginal Munshkin Card Game By:º"
PRINT "º Austin Jackson and Ford King.º"
PRINT "ÈÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍ¼"
3 PRINT
4 PRINT "By what name should I call you?"
INPUT ">", N$
5 PRINT "Hello There, "; N$ + "!"
6 PRINT
PRINT "Are you ready to save Munshkin?"
7 INPUT ">", O$
8 O$ = UCASE$(O$)
9 IF O$ = "YES" THEN
PRINT
10 PRINT "Prepare yourself!"
11 ELSE
PRINT
PRINT "To advance you must reply 'yes'."
12 GOTO 7
13 END IF
14 PRINT
15 PRINT "Commands:"
16 PRINT "N, S, E, W - Moving"
17 PRINT "Look - Print Map Details"
18 PRINT "Exit - End Program"
19 PRINT
20 PRINT "Map Key: "
21 PRINT "Empty - Walking Space"
22 PRINT "Û - Wall/Stopper Space"
23 PRINT
24 PRINT "The Generals Chamber:"
25 PRINT "ÛÛgÛÛ"
26 PRINT "ÛÛ ÛÛ"
27 PRINT "ÛÛ ÛÛ"
28 PRINT "ÛÛuÛÛ"
29 PRINT "ÛÛÛÛÛ"
30 PRINT "g=The General u=You"
PRINT
31 PRINT "Talk to The General to get your assignment."
PRINT "You are standing in a small hallway leading to The Generals desk."
32 INPUT ">", a$
33 a$ = UCASE$(a$)
34 IF a$ = "EXIT" THEN
35 END
36 END IF
37 IF a$ = "LOOK" THEN
38 GOTO 23
39 END IF
IF a$ = "W" THEN
PRINT
PRINT "That was is blocked."
GOTO 32
END IF
IF a$ = "E" THEN
PRINT
PRINT "That was is blocked."
GOTO 32
END IF
40 IF a$ = "S" THEN
PRINT
41 PRINT "That way is blocked."
42 GOTO 32
43 END IF
44 IF a$ = "N" THEN
45 PRINT
46 PRINT "The Generals Chamber:"
47 PRINT "ÛÛgÛÛ"
48 PRINT "ÛÛ ÛÛ"
49 PRINT "ÛÛuÛÛ"
50 PRINT "ÛÛ ÛÛ"
51 PRINT "ÛÛÛÛÛ"
52 PRINT "g=The General u=You"
PRINT
53 PRINT "You see the General 2 steps infront of you."
54 INPUT ">", b$
ELSE
PRINT
PRINT "Not recgonized command."
GOTO 32
END IF
55 b$ = UCASE$(b$)
56 IF b$ = "EXIT" THEN
57 END
58 END IF
59 IF b$ = "LOOK" THEN
60 GOTO 45
61 END IF
IF b$ = "W" THEN
PRINT
PRINT "That was is blocked."
GOTO 54
END IF
IF b$ = "E" THEN
PRINT
PRINT "That was is blocked."
GOTO 54
END IF
62 IF b$ = "S" THEN
64 GOTO 23
65 END IF
IF b$ = "N" THEN
66 PRINT
67 PRINT "The Generals Chamber:"
68 PRINT "ÛÛgÛÛ"
69 PRINT "ÛÛuÛÛ"
70 PRINT "ÛÛ ÛÛ"
71 PRINT "ÛÛ ÛÛ"
72 PRINT "ÛÛÛÛÛ"
73 PRINT "g=The General u=You"
PRINT
74 PRINT "You see the General 1 step infront of you."
75 INPUT ">", c$
ELSE
PRINT
PRINT "Not recgonized command."
GOTO 54
END IF
76 c$ = UCASE$(c$)
77 IF c$ = "EXIT" THEN
78 END
79 END IF
80 IF c$ = "LOOK" THEN
81 GOTO 66
82 END IF
IF c$ = "W" THEN
PRINT
PRINT "That was is blocked."
GOTO 75
END IF
IF c$ = "E" THEN
PRINT
PRINT "That was is blocked."
GOTO 75
END IF
83 IF c$ = "S" THEN
84 GOTO 45
85 END IF
IF c$ = "N" THEN
86 PRINT
87 PRINT "The Generals Chamber:"
89 PRINT "ÛÛgÛÛ"
90 PRINT "ÛÛ ÛÛ"
91 PRINT "ÛÛ ÛÛ"
92 PRINT "ÛÛ ÛÛ"
   PRINT "ÛÛÛÛÛ"
93 PRINT "g=The General"
PRINT
94 PRINT "The General is standing before you. Type hello to recive your mission."
95 INPUT ">", d$
ELSE
PRINT
PRINT "Not recgonized command."
GOTO 75
END IF
96 d$ = UCASE$(d$)
97 IF d$ = "EXIT" THEN
98 END
99 END IF
100 IF d$ = "LOOK" THEN
101 GOTO 95
102 END IF
IF d$ = "W" THEN
PRINT
PRINT "That was is blocked."
GOTO 95
END IF
IF d$ = "S" THEN
PRINT
PRINT "No turning back now! Your infront of the General!"
GOTO 95
END IF
IF d$ = "E" THEN
PRINT
PRINT "That was is blocked."
GOTO 95
END IF
103 IF d$ = "HELLO" THEN
PRINT
104 PRINT "The General: Why hello there! What can I do for you?"
105 PRINT "1. I'm here to save Munshkin!"
106 PRINT "2. Do you have the time..."
107 PRINT "3. Nothing Really."
108 INPUT ">", E$
ELSE
PRINT
PRINT "Not recgonized command."
GOTO 95
END IF
109 E$ = UCASE$(E$)
110 IF E$ = "3" THEN
PRINT
111 PRINT "Are you sure your not here for something?"
112 GOTO 105
113 END IF
114 IF E$ = "2" THEN
PRINT
115 PRINT "Half past two my boy! Are you here for something?"
116 GOTO 105
117 END IF
118 IF E$ = "1" THEN
PRINT
119 PRINT "AH! My lad why didn't you say so!"
120 PRINT "*He hops out of his chair* His true height is now known, he is a munshkin."
121 PRINT "I will tell you the story:"
123 PRINT "Long ago Munshkins roomed free, until THE EVIL CHEESE and his followers Evil"
PRINT "Cupcakes found the Planet of Munshkin. They have infected the country side! But heres the rub, the Evil Muffins only do The Evil Cheeses bidding while he is"
125 PRINT "alive. You must find 'THE CHEESE GRATER OF DOOM' and kill the The Evil Cheese!"
126 PRINT "Do you accecpt this task?"
INPUT ">", F$
ELSE
PRINT
PRINT "Try choosing a number."
GOTO 105
END IF
127 F$ = UCASE$(F$)
128 IF F$ = "YES" THEN
PRINT
129 PRINT "Praise all of Munshkin! You are our savior!"
130 PRINT "Also, take this: *SAMURAI SWORD OBTAINED*!"
147 PRINT "Shall I tele you to The Den of THE CHEESE GRATER OF DOOM?"
INPUT ">", G$
ELSE
PRINT
PRINT "To advance you must reply 'yes'."
GOTO 126
END IF
151 G$ = UCASE$(G$)
152 IF G$ = "YES" THEN
PRINT
PRINT "The small Munshkin takes a small wooden rod out of his pocket and taps you on"
PRINT "the head. *WOOSH!* You fell as though you are sucked through a small tube."
ELSE
PRINT
PRINT "To advance you must reply 'yes'."
GOTO 147
END IF
SLEEP








