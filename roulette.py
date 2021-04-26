import turtle, math, random

winnings = 100

evenNumb = [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36]
oddNumb = [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31,33,35]
fIrst12 = [1,2,3,4,5,6,7,8,9,10,11,12]
scd12 = [13,14,15,16,17,18,19,20,21,22,23,24]
last12 = [25,26,27,28,29,30,31,32,33,34,35,36]
blacknum = [2,4,6,8,10,11,13,15,17,20,22,24,26,28,29,31,33,35]
rednum = [1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36]
betOption = {'EVEN':evenNumb,  'ODD':oddNumb, 'ZERO': 0, '1ST 12': fIrst12, '2ND 12': scd12,'3RD 12':last12, 'RED':rednum, 'BLACK':blacknum }

screen = turtle.Screen()
screen.bgcolor('green')
screen.title('Roulette Game')
screen.setup(1300,750)

bob1 = turtle.Turtle()
bob1.ht()
bob1.pensize(2)
bob1.speed(0)

ball = turtle.Turtle()
ball.speed(0)
ball.shape('circle')
ball.shapesize(1)
ball.color('beige')
ball.penup()

buton = turtle.Turtle()
buton.ht()
buton.speed(0)
buton.color('white')
buton.pensize(3)


bob = turtle.Turtle()
bob.ht()
bob.pensize(2)
bob.speed(0)


chip1 = turtle.Turtle()
chip1.shape('circle')
chip1.color('yellow')
chip1.shapesize(2)
chip1.up()
chip1.setpos(0,-50)
chip1.down()
chip1.stamp()
chip1.up()

chip2 = turtle.Turtle()
chip2.shape('circle')
chip2.color('blue')
chip2.shapesize(2)
chip2.up()
chip2.setpos(50,-50)
chip2.down()
chip2.stamp()
chip2.up()

chip3 = turtle.Turtle()
chip3.shape('circle')
chip3.color('black')
chip3.shapesize(2)
chip3.up()
chip3.setpos(100,-50)
chip3.down()
chip3.stamp()
chip3.up()

win_pos = {(-108.7, 118.41): 0, (-112.39, 155.23): 26, (-122.26, 190.89): 3, (-138.0, 224.37): 35, (-159.18, 254.71): 12, (-185.19, 281.03): 28, (-215.26, 302.58): 7, (-248.55, 318.74): 29, (-284.09, 329.04): 18, (-320.85, 333.18): 22, (-357.79, 331.05): 9, (-393.84, 322.71): 31, (-427.96, 308.4): 14, (-459.17, 288.53): 20, (-486.57, 263.67): 1, (-509.38, 234.53): 33, (-526.93, 201.96): 16, (-538.73, 166.89): 24, (-544.43, 130.33): 5, (-543.88, 93.34): 10, (-537.07, 56.97): 23, (-524.22, 22.27): 8, (-505.69, -9.75): 30, (-482.02, -38.19): 11, (-453.87, -62.21): 36, (-422.08, -81.13): 13, (-387.54, -94.41): 27, (-351.26, -101.65): 6, (-314.27, -102.67): 34, (-277.65, -97.41): 17, (-242.44, -86.05): 25, (-209.65, -68.89): 2, (-180.24, -46.44): 21, (-155.05, -19.35): 4, (-134.79, 11.62): 19, (-120.06, 45.56): 15, (-111.28, 81.5): 32}

angle = 180 - (0.5*(180 - (360/37)))
def radius(n):
    radius = n/(2*math.sin(math.radians(180/37)))
    return  radius

def polygon1(n):
    bob1.color('white')
    for i in range(37):
        bob1.begin_fill()
        bob1.forward(radius(n) )
        bob1.left(angle )
        bob1.forward(n)
        bob1.left(angle )
        bob1.forward(radius(n))
        bob1.left(180)
        bob1.end_fill()

def polygon2(n):
    for i in range(37):
        bob1.begin_fill()
        if i == 0 :
            bob1.color('green')
        elif i in [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31,33,35]:
            bob1.color('black')
        else:
            bob1.color('red')
        bob1.forward(radius(n) )
        bob1.left(angle )
        bob1.forward(n)
        bob1.left(angle )
        bob1.forward(radius(n))
        bob1.left(180)
        bob1.end_fill()

def polygon3(n):
    for j in range(37):
        bob1.color('white')
        bob1.up()
        nblist= [0,26,3,35,12,28,7,29,18,22,9,31,14,20,1,33,16,24,5,10,23,8,30,11,36,13,27,6,34,17,25,2,21,4,19,15,32]
        bob1.forward(radius(n) )
        bob1.left(angle )
        bob1.forward(n)
        bob1.down()
        bob1.write( nblist[j] , font =('Arial',12,'normal'))
        bob1.up()
        bob1.left(angle )
        bob1.forward(radius(n))
        bob1.left(180)
        bob1.down()

def polygon4(n):
    bob1.color('black')
    for i in range(37):
        bob1.forward(radius(n) )
        bob1.left(angle )
        bob1.forward(n)
        bob1.left(angle )
        bob1.forward(radius(n))
        bob1.left(180)


def spin_ball(n):
    d = 0
    ball.setpos(-108.70,118.41)
    ball.right(4)
    ball.left(90)
    m = random.randint(0,36)
    for i in range(m):
        ball.left(360/37)
        ball.forward(n)
    coordX = ball.xcor()
    coordY = ball.ycor()
    pos = (round(coordX, 2),round(coordY, 2))
    if  9 < m < 12 :
        ball.forward(n/3)
    elif 12 <= m <= 14:
        ball.forward(n*(2/3))
    elif 14 < m < 22:
        ball.forward(n)
    elif 22 <= m < 30:
        ball.forward(n/2)
    elif 30 <= m < 32:
        ball.forward(n/3)
    while d != 2:
        for i in range(37):
            ball.left(360/37)
            ball.forward(n)
        d +=1
    return win_pos[pos]

def sqr():
    for i in range(12):
        bob.forward(50)
        bob.left(90)
        bob.forward(50)
        bob.backward(50)
        bob.right(90)

def draw_Board():
    bob.forward(600)
    bob.left(90)
    bob.forward(250)
    bob.left(90)
    bob.forward(600)
    bob.left(90)
    bob.forward(250)
    bob.backward(50)
    bob.left(90)
    for j in range(4):
        bob.forward(150)
        bob.right(90)
        bob.forward(50)
        bob.backward(50)
        bob.left(90)
    bob.left(90)
    bob.forward(50)
    bob.left(90)
    for i in range(3):
        sqr()
        bob.backward(600)
        bob.right(90)
        bob.forward(50)
        bob.left(90)
    for u in range(3):
        bob.forward(200)
        bob.left(90)
        bob.forward(50)
        bob.backward(50)
        bob.right(90)
    bob.left(90)#
    bob.forward(50)
    bob.right(90)
    bob.forward(25)
    bob.left(45)
    bob.forward(25)
    bob.left(45)
    bob.forward(114)
    bob.left(45)
    bob.forward(25)
    bob.left(45)
    bob.forward(25)
    coord = {1:(15,165), 2:(15,115), 3:(15,65), 4:(65,165), 5:(65,115), 6:(65,65), 7:(115,165), 8:(115,115), 9:(115,65), 10:(165,165), 11:(165,115), 12:(165,65), 13:(215,165), 14:(215,115), 15:(215,65), 16:(265,165), 17:(265,115), 18:(265,65), 19:(315,165),  20:(315,115), 21:(315,65), 22:(365,165), 23:(365,115), 24:(365,65), 25:(415,165), 26:(415,115), 27:(415,65), 28:(465,165), 29:(465,115), 30:(465,65), 31:(515,165), 32:(515,115), 33:(515,65), 34:(565,165), 35:(565,115), 36:(565,65)}
    for i in range(1,37):
        bob.penup()
        bob.goto(coord[i])
        bob.pendown()
        if i in [1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36]:
            bob.color('red')
        else:
            bob.color('black')
        bob.write(i, font =('Arial',30,'normal'))
    bob.penup()
    bob.color('white')
    bob.goto(-25,115)
    bob.pendown()
    bob.write( 0 , font =('Arial',30,'normal'))
    bob.penup()
    bob.goto(65,215)
    bob.pendown()
    bob.write( '1st 12' , font =('Arial',30,'normal'))
    bob.penup()
    bob.goto(265,215)
    bob.pendown()
    bob.write( '2nd 12' , font =('Arial',30,'normal'))
    bob.penup()
    bob.goto(465,215)
    bob.pendown()
    bob.write( '3rd 12' , font =('Arial',30,'normal'))

    bob.penup()
    bob.goto(35,15)
    bob.pendown()
    bob.write( 'EVEN' , font =('Arial',30,'normal'))

    bob.penup()
    bob.goto(185,15)
    bob.pendown()
    bob.write( 'ODD' , font =('Arial',30,'normal'))

    bob.penup()
    bob.goto(330,15)
    bob.pendown()
    bob.color('black')
    bob.write( 'BLACK' , font =('Arial',30,'normal'))

    bob.penup()
    bob.goto(495,15)
    bob.pendown()
    bob.color('red')
    bob.write( 'RED' , font =('Arial',30,'normal'))
    bob.hideturtle()

def startupbtt():
    buton.up()
    buton.setpos(0,-100)
    buton.down()
    for i in range(2):
        buton.forward(150)
        buton.right(90)
        buton.forward(50)
        buton.right(90)
    buton.up()
    buton.goto(35,-135)
    buton.down()
    buton.write('PLAY', font =('Arial',30,'normal'))


def resetbtt():
    buton.up()
    buton.setpos(200,-100)
    buton.down()
    for i in range(2):
        buton.forward(150)
        buton.right(90)
        buton.forward(50)
        buton.right(90)
    buton.up()
    buton.goto(235,-135)
    buton.down()
    buton.write('RESET', font =('Arial',30,'normal'))


# CHIPS

def drag1(x,y):
    chip1.ondrag(None)
    chip1.goto(x,y)
    chip1.ondrag(drag1)

def drag2(x,y):
    chip2.ondrag(None)
    chip2.goto(x,y)
    chip2.ondrag(drag2)

def drag3(x,y):
    chip3.ondrag(None)
    chip3.goto(x,y)
    chip3.ondrag(drag3)

def f1():
    coordX = chip1.xcor()
    coordY = chip1.ycor()
    pos = (round(coordX, 2),round(coordY, 2))
    return pos

def f2():
    coordX = chip2.xcor()
    coordY = chip2.ycor()
    pos = (round(coordX, 2),round(coordY, 2))
    return pos

def f3():
    coordX = chip3.xcor()
    coordY = chip3.ycor()
    pos = (round(coordX, 2),round(coordY, 2))
    return pos

def chip_Event(x,y):
    if x == 0 and y == -50:
        chip1.ondrag(drag1)
    elif x == 50 and y == - 50:
        chip2.ondrag(drag2)
    elif x == 100 and y == - 50:
        chip3.ondrag(drag3)



def draw_Wheel():
    bob1.penup()
    bob1.goto(-325,100)
    bob1.pendown()
    polygon1(43)
    polygon2(42)
    bob1.right((360/37)/2)
    polygon3(39)
    bob1.left((360/37)/2)
    polygon1(33)
    polygon4(33)
    bob1.penup()
    bob1.goto(0,0)
    bob1.pendown()

def game_bg():
    draw_Wheel()
    draw_Board()
    startupbtt()
    resetbtt()

def amtAndPos():
    if f1() != (0,-50):
        amtndPos =[f1()[0], f1()[1], 5]
    elif f2() != (50,-50) :
        amtndPos =[f2()[0], f2()[1], 10]
    elif f3() !=  (100,-50):
        amtndPos =[f3()[0], f3()[1], 25]
    return amtndPos


def playEvent(x,y):
    global winnings
    if winnings <= 0:
        print("You lost all your money, better luck next time!")
        screen.bye()
        return
    win = False
    if( x >= 0 and x <= 150) and ( y >= -150 and y <= -100):
        winNumber = spin_ball(37)
        betpos = amtAndPos()
        xbet = betpos[0]
        ybet = betpos[1]
        bet_amount = betpos[2]
        bet = ''
        if (xbet > 0 and xbet< 600) and (ybet > 50 and ybet < 200):
            bet = 'Straight Bet'
            odds = "35:1"
            if (xbet > 0 and xbet < 50):
                if (ybet>50 and ybet<100):
                    betOn = 3
                elif (ybet>100 and ybet<150):
                    betOn = 2
                elif (ybet>150 and ybet<200):
                    betOn = 1

            elif (xbet > 50 and xbet < 100):
                if (ybet>50 and ybet<100):
                    betOn = 6
                elif (ybet>100 and ybet<150):
                    betOn = 5
                elif (ybet >150 and ybet<200) :
                    betOn = 4

            elif (xbet > 100 and xbet < 150):
                if (ybet>50 and ybet<100):
                    betOn = 9
                elif (ybet>100 and ybet<150):
                    betOn = 8
                elif (ybet>150 and ybet<200):
                    betOn = 7

            elif (xbet > 150 and xbet < 200):
                if (ybet>50 and ybet<100):
                    betOn = 12
                elif (ybet>100 and ybet<150):
                    betOn = 11
                elif (ybet>150 and ybet<200):
                    betOn = 10

            elif (xbet > 200 and xbet < 250):
                if (ybet>50 and ybet<100):
                    betOn = 15
                elif (ybet>100 and ybet<150):
                    betOn = 14
                elif (ybet>150 and ybet<200):
                    betOn = 13

            elif (xbet > 250 and xbet < 300):
                if (ybet>50 and ybet<100):
                    betOn = 18
                elif (ybet>100 and ybet<150):
                    betOn = 17
                elif (ybet>150 and ybet<200):
                    betOn = 16

            elif (xbet >300 and xbet<350):
                if (ybet>50 and ybet<100):
                    betOn = 21
                elif (ybet>100 and ybet<150):
                    betOn = 20
                elif (ybet>150 and ybet<200):
                    betOn = 19

            elif (xbet > 350 and xbet < 400):
                if (ybet>50 and ybet<100):
                    betOn = 24
                elif (ybet>100 and ybet<150):
                    betOn = 23
                elif (ybet>150 and ybet<200):
                    betOn = 22

            elif (xbet > 400 and xbet < 450):
                if (ybet>50 and ybet<100):
                    betOn = 27
                elif (ybet>100 and ybet<150):
                    betOn = 26
                elif (ybet>150 and ybet<200):
                    betOn = 25


            elif (xbet > 450 and xbet < 500):
                if (ybet>50 and ybet<100):
                    betOn = 29
                elif (ybet>100 and ybet<150):
                    betOn = 28
                elif (ybet>150 and ybet<200):
                    betOn = 27

            elif (x>500 and x<550):
                if (ybet>50 and ybet<100):
                    betOn = 33
                elif (ybet>100 and ybet<150):
                    betOn = 31
                elif (ybet>150 and ybet<200):
                    betOn = 30

            elif (xbet > 550 and xbet < 600):
                if (ybet>50 and ybet<100):
                    betOn = 36
                elif (ybet>100 and ybet<150):
                    betOn = 35
                elif (ybet>150 and ybet<200):
                    betOn = 34

            if betOn == winNumber:
                win = True
                payout = bet_amount*35

        elif (xbet > 0 and xbet < 600) and (ybet>0 and ybet<50):
            bet = 'Outside Bet'
            odds = "1:1"
            if (xbet >0 and xbet <150):
                betOn = 'EVEN'
            elif (xbet >150 and xbet <300):
                betOn = 'ODD'
            elif (xbet >300 and xbet <450):
                betOn = 'BLACK'
            elif (xbet >450 and xbet <600):
                betOn = 'RED'

            if winNumber in betOption[betOn]:
                win = True
                payout = bet_amount*2

        elif (xbet > 0 and xbet < 600) and (ybet>200 and ybet<250):
            bet = 'Outside Bet'
            odds = "2:1"
            if (xbet >0 and xbet <200):
                betOn = '1ST 12'
            elif (xbet >200 and xbet <400):
                betOn = '2ND 12'
            elif (xbet >400 and xbet <600):
                betOn = '3RD 12'

            if winNumber in betOption[betOn]:
                win = True
                payout = bet_amount*3

        elif (xbet > -50 and xbet <0) and (ybet>50 and ybet<200):
            bet = 'ZERO'
            betOn = 0
        print('You bet ' + str(bet_amount) + ' dollars on ' + str(betOn) + '. This is a ' + str(bet) + ', so the odds are ' + odds)
        print("The winning number is " + str(winNumber))
        if win == True:
            winnings += payout
            print("You won! Your payout is $" + str(payout) + ". You now have $" + str(winnings))
        else:
            winnings -= bet_amount
            print("You lost! Try again. You now have $" + str(winnings))



    elif( x >= 200 and x <= 350) and ( y >= -150 and y <= -100):
        chip1.setpos(0,-50)
        chip2.setpos(50,-50)
        chip3.setpos(100,-50)
        ball.reset()
        ball.speed(0)
        ball.shape('circle')
        ball.shapesize(1)
        ball.color('beige')
        ball.penup()



#    Set the graphics of the game.
game_bg()


def ask():
    while True:
        again = input("Type 'Exit' at any time to cash out ")
        again = again.upper()
        if again == "EXIT":
            screen.bye()
            return True
        else:
            pass

print("Welcome to Roulette! You start with $100!")
print("To play: Drag a chip onto the board to place a bet, then hit PLAY to spin the wheel! (Yellow = $5, Blue = $10, Black = $25)")
print("To replay: Hit RESET, Drag a chip onto the board to place a bet, then hit PLAY to spin the wheel! (Yellow = $5, Blue = $10, Black = $25)")

turn = False
while turn == False:

    chip1.ondrag(drag1)
    chip2.ondrag(drag2)
    chip3.ondrag(drag3)
    screen.onclick(playEvent)
    screen.listen()
    turn = ask()
print("Goodbye! You cashed out with $" + str(winnings) )
