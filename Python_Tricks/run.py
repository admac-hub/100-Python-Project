from turtle import *
import turtle as tur
# To hide turtle

def future_gf():
    intro = print('Hey! :')
    build_up = print('Wanted to ask you a question : ')
    print('Ummm, I like you a lot')
    prop = input('do you want to be my girlfriend ? (y/n): ')
    accept = False
    while not accept:
        if prop == 'y':
            turt = tur.Turtle()
            tur.title("Pythontpoint")
            def curve():
                for i in range(200):
                    # Defining step by step curve motion
                    turt.right(1)
                    turt.forward(1)
            def heart():
                # Set the fill color to red
                turt.fillcolor('red')
                # Start filling the color
                turt.begin_fill()
                turt.left(140)
                turt.forward(113)
                curve()
                turt.left(120)
                # Draw the right curve
                curve()
                turt.forward(112)
                turt.end_fill()
            def txt():
                turt.up()
                turt.setpos(-68, 95)
                turt.down()
                turt.color('cyan')
                turt.write("I Love You", font=(
                "Times New Roman", 12, "bold"))
            heart()
            txt()
            tur.ht()
            tur.done() 
            accept = True
        else:
            prop = input('wrong answer, please try again unitl you change your say yes :')
future_gf()