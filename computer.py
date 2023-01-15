# from replit import audio
import time
import os
import random
import turtle
from turtle import Screen
import math
from datetime import datetime
import pytz
import numbers

# Try to make a smartphone/computer with many different applications, either using colorblocks or turtle

# x = float(input("What number do you want X to be? "))
# y = float(5)

# exp = float(5*(x)**7 -8 + 909)

# print(f"The soultion is {exp}")
# print(f"X is {x}")

# source = audio.play_file('LIMINAL _ kian ft. KAFU (original song).mp3')

# while True:
#  pass

# Colors for the fill command
bg_col = "#00a2ed"
comp_bar_col = "#373433"

# initilization
screen = Screen()

# global stuff
global cal_helper1
global cal_helper2
global firstnum
global operators
global addition
global subtraction
global multiplication
global division
global secondnum
global x
global y
cal_helper1 = turtle.Turtle()
cal_helper2 = turtle.Turtle()
firstnum = "0"
operators = "0"
addition = False
subtraction = False
division = False
multiplication = False
secondnum = "0"
x = float(0)
y = float(0)


def num1clear():
    cal_helper1.clear()


# When you press C, it opens the calculator application. Only Once.
def c():
    screen.onkey(None, "c")
    calc.hideturtle()
    calc.color("black")
    calc.clear()
    calc.right(90)
    calc.forward(90)
    calc.right(90)
    calc.penup()
    calc.forward(85)
    calc.pendown()
    calc.forward(240)
    calc.right(90)
    calc.forward(238)
    calc.right(90)
    calc.forward(240)
    calc.right(90)
    calc.forward(238)
    calc.penup()
    calc.right(90)
    calc.forward(10)
    calc.right(90)
    calc.forward(15)
    calc.right(-90)
    calc.pendown()
    calc.forward(220)
    calc.right(90)
    calc.forward(40)
    calc.right(90)
    calc.forward(220)
    calc.right(90)
    calc.forward(40)
    calc.penup()
    calc.right(90)
    calc.forward(18)
    calc.forward(50)
    calc.right(90)
    calc.forward(60)
    calc.right(90)
    calc.forward(63)
    calc.right(-90)
    calc.pendown()
    calc.forward(25)
    calc.right(-90)
    calc.forward(55)
    calc.right(-90)
    calc.forward(25)
    calc.right(-90)
    calc.forward(55)
    calc.penup()
    calc.backward(75)
    calc.right(-90)
    calc.pendown()
    calc.forward(25)
    calc.right(-90)
    calc.forward(55)
    calc.right(-90)
    calc.forward(25)
    calc.right(-90)
    calc.forward(55)
    calc.penup()
    calc.backward(75)
    calc.right(-90)
    calc.pendown()
    calc.forward(25)
    calc.right(-90)
    calc.forward(55)
    calc.right(-90)
    calc.forward(25)
    calc.right(-90)
    calc.forward(55)
    calc.right(-90)
    calc.penup()
    calc.forward(35)
    calc.right(90)
    calc.forward(150)
    calc.right(-90)
    calc.pendown()
    calc.forward(25)
    calc.right(-90)
    calc.forward(55)
    calc.right(-90)
    calc.forward(25)
    calc.right(-90)
    calc.forward(55)
    calc.penup()
    calc.backward(75)
    calc.pendown()
    calc.right(-90)
    calc.forward(25)
    calc.right(-90)
    calc.forward(55)
    calc.right(-90)
    calc.forward(25)
    calc.right(-90)
    calc.forward(55)
    calc.penup()
    calc.backward(75)
    calc.pendown()
    calc.right(-90)
    calc.forward(25)
    calc.right(-90)
    calc.forward(55)
    calc.right(-90)
    calc.forward(25)
    calc.right(-90)
    calc.forward(55)
    calc.right(-90)
    calc.penup()
    calc.forward(35)
    calc.right(90)
    calc.forward(150)
    calc.pendown()
    calc.right(90)
    calc.right(90)
    calc.forward(55)
    calc.right(90)
    calc.forward(25)
    calc.right(90)
    calc.forward(55)
    calc.right(90)
    calc.forward(25)
    calc.right(90)
    calc.penup()
    calc.forward(75)
    calc.pendown()
    calc.forward(55)
    calc.right(90)
    calc.forward(25)
    calc.right(90)
    calc.forward(55)
    calc.right(90)
    calc.forward(25)
    calc.right(90)
    calc.penup()
    calc.right(90)
    calc.right(-90)
    calc.forward(75)
    calc.pendown()
    calc.pendown()
    calc.forward(55)
    calc.right(90)
    calc.forward(25)
    calc.right(90)
    calc.forward(55)
    calc.right(90)
    calc.forward(25)
    calc.right(90)
    calc.penup()
    calc.right(90)
    calc.forward(35)
    calc.right(90)
    calc.forward(150)
    calc.right(-90)
    calc.pendown()
    calc.forward(25)
    calc.right(-90)
    calc.forward(55)
    calc.right(-90)
    calc.forward(25)
    calc.right(-90)
    calc.forward(55)
    calc.penup()
    calc.backward(75)
    calc.pendown()
    calc.right(-90)
    calc.forward(25)
    calc.right(-90)
    calc.forward(55)
    calc.right(-90)
    calc.forward(25)
    calc.right(-90)
    calc.forward(55)
    calc.penup()
    calc.backward(75)
    calc.pendown()
    calc.right(-90)
    calc.forward(25)
    calc.right(-90)
    calc.forward(55)
    calc.right(-90)
    calc.forward(25)
    calc.right(-90)
    calc.forward(55)
    calc.penup()
    calc.right(90)
    calc.right(90)
    calc.forward(63)
    calc.right(90)
    calc.forward(58)
    calc.right(-180)
    calc.pendown()
    calc.forward(25)
    calc.right(-90)
    calc.forward(220)
    calc.right(-90)
    calc.forward(25)
    calc.penup()
    calc.right(-180)
    calc.right(-180)
    calc.forward(5)
    calc.right(-90)
    calc.forward(113)
    calc.color("white")
    calc.write("CASIO", False, align="center", font=("Eurostile", 22, "bold"))
    calc.penup()
    calc.color("black")
    calc.right(-90)
    calc.forward(137)
    calc.right(-90)
    calc.forward(77)
    calc.color("white")
    calc.write("7", False, align="center", font=("Century Gothic", 23))
    calc.backward(75)
    calc.write("8", False, align="center", font=("Century Gothic", 23))
    calc.backward(75)
    calc.write("9", False, align="center", font=("Century Gothic", 23))
    calc.right(-90)
    calc.forward(36)
    calc.right(90)
    calc.forward(148)
    calc.write("4", False, align="center", font=("Century Gothic", 23))
    calc.backward(75)
    calc.write("5", False, align="center", font=("Century Gothic", 23))
    calc.backward(64)
    calc.write("6", False, align="left", font=("Gothic Century", 23))
    calc.right(-90)
    calc.forward(35)
    calc.right(90)
    calc.forward(148)
    calc.write("1", False, align="left", font=("Gothic Century", 23))
    calc.backward(83)
    calc.write("2", False, align="center", font=("Gothic Century", 23))
    calc.backward(75)
    calc.write("3", False, align="center", font=("Gothic Century", 23))
    calc.right(-90)
    calc.forward(35)
    calc.right(90)
    calc.forward(153)
    calc.write("AC", False, align="center", font=("Gothic Century", 23))
    calc.backward(78)
    calc.write("0", False, align="center", font=("Gothic Century", 23))
    calc.backward(60)
    calc.write("=", False, align="left", font=("Gothic Century", 25))
    calc.right(90)
    calc.forward(153)
    calc.right(90)
    calc.forward(45)


# First number for calculator
if firstnum == "0":
    def first1():
        screen.onkey(None, "1")
        screen.onkey(None, "2")
        screen.onkey(None, "3")
        screen.onkey(None, "4")
        screen.onkey(None, "5")
        screen.onkey(None, "6")
        screen.onkey(None, "7")
        screen.onkey(None, "8")
        screen.onkey(None, "9")
        screen.onkey(None, "0")

        x = float(1)
        cal_helper1.hideturtle()
        cal_helper1.pen(speed=125)
        cal_helper1.right(-90)
        cal_helper1.penup()
        cal_helper1.forward(216)
        cal_helper1.right(90)
        cal_helper1.forward(93)
        cal_helper1.color("white")
        cal_helper1.write(f"{x}", True, align="right",
                          font=("Gothic Century", 30))

    def first2():
        screen.onkey(None, "1")
        screen.onkey(None, "2")
        screen.onkey(None, "3")
        screen.onkey(None, "4")
        screen.onkey(None, "5")
        screen.onkey(None, "6")
        screen.onkey(None, "7")
        screen.onkey(None, "8")
        screen.onkey(None, "9")
        screen.onkey(None, "0")

        x = float(2)
        cal_helper1.hideturtle()
        cal_helper1.pen(speed=125)
        cal_helper1.right(-90)
        cal_helper1.penup()
        cal_helper1.forward(216)
        cal_helper1.right(90)
        cal_helper1.forward(93)
        cal_helper1.color("white")
        cal_helper1.write(f"{x}", True, align="right",
                          font=("Gothic Century", 30))

    def first3():
        screen.onkey(None, "1")
        screen.onkey(None, "2")
        screen.onkey(None, "3")
        screen.onkey(None, "4")
        screen.onkey(None, "5")
        screen.onkey(None, "6")
        screen.onkey(None, "7")
        screen.onkey(None, "8")
        screen.onkey(None, "9")
        screen.onkey(None, "0")

        x = float(3)
        cal_helper1.hideturtle()
        cal_helper1.pen(speed=125)
        cal_helper1.right(-90)
        cal_helper1.penup()
        cal_helper1.forward(216)
        cal_helper1.right(90)
        cal_helper1.forward(93)
        cal_helper1.color("white")
        cal_helper1.write(f"{x}", True, align="right",
                          font=("Gothic Century", 30))

    def first4():
        screen.onkey(None, "1")
        screen.onkey(None, "2")
        screen.onkey(None, "3")
        screen.onkey(None, "4")
        screen.onkey(None, "5")
        screen.onkey(None, "6")
        screen.onkey(None, "7")
        screen.onkey(None, "8")
        screen.onkey(None, "9")
        screen.onkey(None, "0")

        x = float(4)
        cal_helper1.hideturtle()
        cal_helper1.pen(speed=125)
        cal_helper1.right(-90)
        cal_helper1.penup()
        cal_helper1.forward(216)
        cal_helper1.right(90)
        cal_helper1.forward(93)
        cal_helper1.color("white")
        cal_helper1.write(f"{x}", True, align="right",
                          font=("Gothic Century", 30))

    def first5():
        screen.onkey(None, "1")
        screen.onkey(None, "2")
        screen.onkey(None, "3")
        screen.onkey(None, "4")
        screen.onkey(None, "5")
        screen.onkey(None, "6")
        screen.onkey(None, "7")
        screen.onkey(None, "8")
        screen.onkey(None, "9")
        screen.onkey(None, "0")

        x = float(5)
        cal_helper1.hideturtle()
        cal_helper1.pen(speed=125)
        cal_helper1.right(-90)
        cal_helper1.penup()
        cal_helper1.forward(216)
        cal_helper1.right(90)
        cal_helper1.forward(93)
        cal_helper1.color("white")
        cal_helper1.write(f"{x}", True, align="right",
                          font=("Gothic Century", 30))

    def first6():
        screen.onkey(None, "1")
        screen.onkey(None, "2")
        screen.onkey(None, "3")
        screen.onkey(None, "4")
        screen.onkey(None, "5")
        screen.onkey(None, "6")
        screen.onkey(None, "7")
        screen.onkey(None, "8")
        screen.onkey(None, "9")
        screen.onkey(None, "0")

        x = float(6)
        cal_helper1.hideturtle()
        cal_helper1.pen(speed=125)
        cal_helper1.right(-90)
        cal_helper1.penup()
        cal_helper1.forward(216)
        cal_helper1.right(90)
        cal_helper1.forward(93)
        cal_helper1.color("white")
        cal_helper1.write(f"{x}", True, align="right",
                          font=("Gothic Century", 30))

    def first7():
        screen.onkey(None, "1")
        screen.onkey(None, "2")
        screen.onkey(None, "3")
        screen.onkey(None, "4")
        screen.onkey(None, "5")
        screen.onkey(None, "6")
        screen.onkey(None, "7")
        screen.onkey(None, "8")
        screen.onkey(None, "9")
        screen.onkey(None, "0")

        x = float(7)
        cal_helper1.hideturtle()
        cal_helper1.pen(speed=125)
        cal_helper1.right(-90)
        cal_helper1.penup()
        cal_helper1.forward(216)
        cal_helper1.right(90)
        cal_helper1.forward(93)
        cal_helper1.color("white")
        cal_helper1.write(f"{x}", True, align="right",
                          font=("Gothic Century", 30))

    def first8():
        screen.onkey(None, "1")
        screen.onkey(None, "2")
        screen.onkey(None, "3")
        screen.onkey(None, "4")
        screen.onkey(None, "5")
        screen.onkey(None, "6")
        screen.onkey(None, "7")
        screen.onkey(None, "8")
        screen.onkey(None, "9")
        screen.onkey(None, "0")

        x = float(8)
        cal_helper1.hideturtle()
        cal_helper1.pen(speed=125)
        cal_helper1.right(-90)
        cal_helper1.penup()
        cal_helper1.forward(216)
        cal_helper1.right(90)
        cal_helper1.forward(93)
        cal_helper1.color("white")
        cal_helper1.write(f"{x}", True, align="right",
                          font=("Gothic Century", 30))

    def first9():
        screen.onkey(None, "1")
        screen.onkey(None, "2")
        screen.onkey(None, "3")
        screen.onkey(None, "4")
        screen.onkey(None, "5")
        screen.onkey(None, "6")
        screen.onkey(None, "7")
        screen.onkey(None, "8")
        screen.onkey(None, "9")
        screen.onkey(None, "0")

        x = float(9)
        cal_helper1.hideturtle()
        cal_helper1.pen(speed=125)
        cal_helper1.right(-90)
        cal_helper1.penup()
        cal_helper1.forward(216)
        cal_helper1.right(90)
        cal_helper1.forward(93)
        cal_helper1.color("white")
        cal_helper1.write(f"{x}", True, align="right",
                          font=("Gothic Century", 30))

    def first0():
        screen.onkey(None, "1")
        screen.onkey(None, "2")
        screen.onkey(None, "3")
        screen.onkey(None, "4")
        screen.onkey(None, "5")
        screen.onkey(None, "6")
        screen.onkey(None, "7")
        screen.onkey(None, "8")
        screen.onkey(None, "9")
        screen.onkey(None, "0")

        x = float(0)
        cal_helper1.hideturtle()
        cal_helper1.pen(speed=125)
        cal_helper1.right(-90)
        cal_helper1.penup()
        cal_helper1.forward(216)
        cal_helper1.right(90)
        cal_helper1.forward(93)
        cal_helper1.color("white")
        cal_helper1.write(f"{x}", True, align="right",
                          font=("Gothic Century", 30))

    def negnum():

        def neg1():
            x = float(-1)

            screen.onkey(None, "1")
            screen.onkey(None, "2")
            screen.onkey(None, "3")
            screen.onkey(None, "4")
            screen.onkey(None, "5")
            screen.onkey(None, "6")
            screen.onkey(None, "7")
            screen.onkey(None, "8")
            screen.onkey(None, "9")
            screen.onkey(None, "0")

            cal_helper1.hideturtle()
            cal_helper1.pen(speed=125)
            cal_helper1.right(-90)
            cal_helper1.penup()
            cal_helper1.forward(216)
            cal_helper1.right(90)
            cal_helper1.forward(93)
            cal_helper1.color("white")
            cal_helper1.write(f"{x}", True, align="right",
                              font=("Gothic Century", 30))

        def neg2():
            x = float(-2)
            cal_helper1.hideturtle()
            cal_helper1.pen(speed=125)
            cal_helper1.right(-90)
            cal_helper1.penup()
            cal_helper1.forward(216)
            cal_helper1.right(90)
            cal_helper1.forward(93)
            cal_helper1.color("white")
            cal_helper1.write(f"{x}", True, align="right",
                              font=("Gothic Century", 30))

        def neg3():
            x = float(-3)
            cal_helper1.hideturtle()
            cal_helper1.pen(speed=125)
            cal_helper1.right(-90)
            cal_helper1.penup()
            cal_helper1.forward(216)
            cal_helper1.right(90)
            cal_helper1.forward(93)
            cal_helper1.color("white")
            cal_helper1.write(f"{x}", True, align="right",
                              font=("Gothic Century", 30))

        def neg4():
            x = float(-4)
            cal_helper1.hideturtle()
            cal_helper1.pen(speed=125)
            cal_helper1.right(-90)
            cal_helper1.penup()
            cal_helper1.forward(216)
            cal_helper1.right(90)
            cal_helper1.forward(93)
            cal_helper1.color("white")
            cal_helper1.write(f"{x}", True, align="right",
                              font=("Gothic Century", 30))

        def neg5():
            x = float(-5)
            cal_helper1.hideturtle()
            cal_helper1.pen(speed=125)
            cal_helper1.right(-90)
            cal_helper1.penup()
            cal_helper1.forward(216)
            cal_helper1.right(90)
            cal_helper1.forward(93)
            cal_helper1.color("white")
            cal_helper1.write(f"{x}", True, align="right",
                              font=("Gothic Century", 30))

        def neg6():
            x = float(-6)
            cal_helper1.hideturtle()
            cal_helper1.pen(speed=125)
            cal_helper1.right(-90)
            cal_helper1.penup()
            cal_helper1.forward(216)
            cal_helper1.right(90)
            cal_helper1.forward(93)
            cal_helper1.color("white")
            cal_helper1.write(f"{x}", True, align="right",
                              font=("Gothic Century", 30))

        def neg7():
            x = float(-7)
            cal_helper1.hideturtle()
            cal_helper1.pen(speed=125)
            cal_helper1.right(-90)
            cal_helper1.penup()
            cal_helper1.forward(216)
            cal_helper1.right(90)
            cal_helper1.forward(93)
            cal_helper1.color("white")
            cal_helper1.write(f"{x}", True, align="right",
                              font=("Gothic Century", 30))

        def neg8():
            x = float(-8)
            cal_helper1.hideturtle()
            cal_helper1.pen(speed=125)
            cal_helper1.right(-90)
            cal_helper1.penup()
            cal_helper1.forward(216)
            cal_helper1.right(90)
            cal_helper1.forward(93)
            cal_helper1.color("white")
            cal_helper1.write(f"{x}", True, align="right",
                              font=("Gothic Century", 30))

        def neg9():
            x = float(-9)
            cal_helper1.hideturtle()
            cal_helper1.pen(speed=125)
            cal_helper1.right(-90)
            cal_helper1.penup()
            cal_helper1.forward(216)
            cal_helper1.right(90)
            cal_helper1.forward(93)
            cal_helper1.color("white")
            cal_helper1.write(f"{x}", True, align="right",
                              font=("Gothic Century", 30))

        def neg0():
            x = float(0)
            cal_helper1.hideturtle()
            cal_helper1.pen(speed=125)
            cal_helper1.right(-90)
            cal_helper1.penup()
            cal_helper1.forward(216)
            cal_helper1.right(90)
            cal_helper1.forward(93)
            cal_helper1.color("white")
            cal_helper1.write(f"{x}", True, align="right",
                              font=("Gothic Century", 30))

        screen.onkey(neg1, "1")
        screen.onkey(neg2, "2")
        screen.onkey(neg3, "3")
        screen.onkey(neg4, "4")
        screen.onkey(neg5, "5")
        screen.onkey(neg6, "6")
        screen.onkey(neg7, "7")
        screen.onkey(neg8, "8")
        screen.onkey(neg9, "9")
        screen.onkey(neg0, "0")

    def check():
        if float(x) < float(0):
            screen.onkey(None, "1")
            screen.onkey(None, "2")
            screen.onkey(None, "3")
            screen.onkey(None, "4")
            screen.onkey(None, "5")
            screen.onkey(None, "6")
            screen.onkey(None, "7")
            screen.onkey(None, "8")
            screen.onkey(None, "9")
            screen.onkey(None, "0")

            firstnum = "1"

        elif float(x) >= float(0):
            screen.onkey(None, "1")
            screen.onkey(None, "2")
            screen.onkey(None, "3")
            screen.onkey(None, "4")
            screen.onkey(None, "5")
            screen.onkey(None, "6")
            screen.onkey(None, "7")
            screen.onkey(None, "8")
            screen.onkey(None, "9")
            screen.onkey(None, "0")

            firstnum = "1"

        turtle.ontimer(check, 5000)
    # Checks the number keys for cal function

    screen.onkey(first1, "1")
    screen.onkey(first2, "2")
    screen.onkey(first3, "3")
    screen.onkey(first4, "4")
    screen.onkey(first5, "5")
    screen.onkey(first6, "6")
    screen.onkey(first7, "7")
    screen.onkey(first8, "8")
    screen.onkey(first9, "9")
    screen.onkey(first0, "0")
    screen.onkey(negnum, "n")


# The operators
if operators == "0":
    def add():
        screen.onkey(k, "equal")
        screen.onkey(k, "minus")
        screen.onkey(k, "slash")
        screen.onkey(k, "x")

        add = turtle.Turtle()
        add.color("white")
        add.penup()
        add.right(-90)
        add.forward(216)
        add.right(-90)
        add.forward(85)
        add.write("+", True, align="right", font=("Gothic Century", 30))
        addition = True

    def sub():
        screen.onkey(k, "equal")
        screen.onkey(k, "slash")
        screen.onkey(k, "minus")
        screen.onkey(k, "x")

        sub = turtle.Turtle()
        sub.color("white")
        sub.penup()
        sub.right(-90)
        sub.forward(214)
        sub.right(-90)
        sub.forward(95)
        sub.write("-", True, align="right", font=("Gothic Century", 35))
        subtraction = True

    def div():
        screen.onkey(k, "equal")
        screen.onkey(k, "minus")
        screen.onkey(k, "slash")
        screen.onkey(k, "x")

        div = turtle.Turtle()
        div.color("white")
        div.penup()
        div.right(-90)
        div.forward(214)
        div.right(-90)
        div.forward(85)
        div.write("÷", True, align="right", font=("Gothic Century", 33))
        division = True

    def mul():
        screen.onkey(k, "equal")
        screen.onkey(k, "minus")
        screen.onkey(k, "slash")
        screen.onkey(k, "x")

        mul = turtle.Turtle()
        mul.color("white")
        mul.penup()
        mul.right(-90)
        mul.forward(203)
        mul.right(-90)
        mul.forward(90)
        mul.write("*", True, align="right", font=("Gothic Century", 35))
        multiplication = True

    screen.onkey(add, "equal")
    screen.onkey(sub, "minus")
    screen.onkey(div, "slash")
    screen.onkey(mul, "x")

    if addition == True:
        operators = "1"
    elif subtraction == True:
        operators = "1"
    elif multiplication == True:
        operators = "1"
    elif division == True:
        operators = "1"


# Second calculator number
def check2():
    screen.textinput("Hello!", "Welcome to your new computer")
    if firstnum == "1" and operators == "1":
        screen.textinput("Hello!", "Welcome to your new computer")

        def second1():
            num1clear()
            screen.onkey(None, "1")
            screen.onkey(None, "2")
            screen.onkey(None, "3")
            screen.onkey(None, "4")
            screen.onkey(None, "5")
            screen.onkey(None, "6")
            screen.onkey(None, "7")
            screen.onkey(None, "8")
            screen.onkey(None, "9")
            screen.onkey(None, "0")

            y = float(1)

            cal_helper2.hideturtle()
            cal_helper2.pen(speed=125)
            cal_helper2.right(-90)
            cal_helper2.penup()
            cal_helper2.forward(216)
            cal_helper2.right(90)
            cal_helper2.forward(93)
            cal_helper2.color("white")
            cal_helper2.write(f"{y}", True, align="right",
                              font=("Gothic Century", 30))
            secondnum = "1"

        def second2():
            cal_helper1.reset()
            cal_helper1.hideturtle()
            screen.onkey(None, "1")
            screen.onkey(None, "2")
            screen.onkey(None, "3")
            screen.onkey(None, "4")
            screen.onkey(None, "5")
            screen.onkey(None, "6")
            screen.onkey(None, "7")
            screen.onkey(None, "8")
            screen.onkey(None, "9")
            screen.onkey(None, "0")

            y = float(2)

            cal_helper2.hideturtle()
            cal_helper2.pen(speed=125)
            cal_helper2.right(-90)
            cal_helper2.penup()
            cal_helper2.forward(216)
            cal_helper2.right(90)
            cal_helper2.forward(93)
            cal_helper2.color("white")
            cal_helper2.write(f"{y}", True, align="right",
                              font=("Gothic Century", 30))
            secondnum = "1"

        def second3():
            cal_helper1.reset()
            cal_helper1.hideturtle()
            screen.onkey(None, "1")
            screen.onkey(None, "2")
            screen.onkey(None, "3")
            screen.onkey(None, "4")
            screen.onkey(None, "5")
            screen.onkey(None, "6")
            screen.onkey(None, "7")
            screen.onkey(None, "8")
            screen.onkey(None, "9")
            screen.onkey(None, "0")

            y = float(3)

            cal_helper2.hideturtle()
            cal_helper2.pen(speed=125)
            cal_helper2.right(-90)
            cal_helper2.penup()
            cal_helper2.forward(216)
            cal_helper2.right(90)
            cal_helper2.forward(93)
            cal_helper2.color("white")
            cal_helper2.write(f"{y}", True, align="right",
                              font=("Gothic Century", 30))
            secondnum = "1"

        def second4():
            cal_helper1.reset()
            cal_helper1.hideturtle()
            screen.onkey(None, "1")
            screen.onkey(None, "2")
            screen.onkey(None, "3")
            screen.onkey(None, "4")
            screen.onkey(None, "5")
            screen.onkey(None, "6")
            screen.onkey(None, "7")
            screen.onkey(None, "8")
            screen.onkey(None, "9")
            screen.onkey(None, "0")

            y = float(4)

            cal_helper2.hideturtle()
            cal_helper2.pen(speed=125)
            cal_helper2.right(-90)
            cal_helper2.penup()
            cal_helper2.forward(216)
            cal_helper2.right(90)
            cal_helper2.forward(93)
            cal_helper2.color("white")
            cal_helper2.write(f"{y}", True, align="right",
                              font=("Gothic Century", 30))
            secondnum = "1"

        def second5():
            cal_helper1.reset()
            cal_helper1.hideturtle()
            screen.onkey(None, "1")
            screen.onkey(None, "2")
            screen.onkey(None, "3")
            screen.onkey(None, "4")
            screen.onkey(None, "5")
            screen.onkey(None, "6")
            screen.onkey(None, "7")
            screen.onkey(None, "8")
            screen.onkey(None, "9")
            screen.onkey(None, "0")
            y = float(5)

            cal_helper2.hideturtle()
            cal_helper2.pen(speed=125)
            cal_helper2.right(-90)
            cal_helper2.penup()
            cal_helper2.forward(216)
            cal_helper2.right(90)
            cal_helper2.forward(93)
            cal_helper2.color("white")
            cal_helper2.write(f"{y}", True, align="right",
                              font=("Gothic Century", 30))
            secondnum = "1"

        def second6():
            cal_helper1.reset()
            cal_helper1.hideturtle()
            screen.onkey(None, "1")
            screen.onkey(None, "2")
            screen.onkey(None, "3")
            screen.onkey(None, "4")
            screen.onkey(None, "5")
            screen.onkey(None, "6")
            screen.onkey(None, "7")
            screen.onkey(None, "8")
            screen.onkey(None, "9")
            screen.onkey(None, "0")

            y = float(6)

            cal_helper2.hideturtle()
            cal_helper2.pen(speed=125)
            cal_helper2.right(-90)
            cal_helper2.penup()
            cal_helper2.forward(216)
            cal_helper2.right(90)
            cal_helper2.forward(93)
            cal_helper2.color("white")
            cal_helper2.write(f"{y}", True, align="right",
                              font=("Gothic Century", 30))
            secondnum = "1"

        def second7():
            cal_helper1.reset()
            cal_helper1.hideturtle()
            screen.onkey(None, "1")
            screen.onkey(None, "2")
            screen.onkey(None, "3")
            screen.onkey(None, "4")
            screen.onkey(None, "5")
            screen.onkey(None, "6")
            screen.onkey(None, "7")
            screen.onkey(None, "8")
            screen.onkey(None, "9")
            screen.onkey(None, "0")

            y = float(7)

            cal_helper2.hideturtle()
            cal_helper2.pen(speed=125)
            cal_helper2.right(-90)
            cal_helper2.penup()
            cal_helper2.forward(216)
            cal_helper2.right(90)
            cal_helper2.forward(93)
            cal_helper2.color("white")
            cal_helper2.write(f"{y}", True, align="right",
                              font=("Gothic Century", 30))
            secondnum = "1"

        def second8():
            cal_helper1.reset()
            cal_helper1.hideturtle()
            screen.onkey(None, "1")
            screen.onkey(None, "2")
            screen.onkey(None, "3")
            screen.onkey(None, "4")
            screen.onkey(None, "5")
            screen.onkey(None, "6")
            screen.onkey(None, "7")
            screen.onkey(None, "8")
            screen.onkey(None, "9")
            screen.onkey(None, "0")

            y = float(8)

            cal_helper2.hideturtle()
            cal_helper2.pen(speed=125)
            cal_helper2.right(-90)
            cal_helper2.penup()
            cal_helper2.forward(216)
            cal_helper2.right(90)
            cal_helper2.forward(93)
            cal_helper2.color("white")
            cal_helper2.write(f"{y}", True, align="right",
                              font=("Gothic Century", 30))
            secondnum = "1"

        def second9():
            cal_helper1.reset()
            cal_helper1.hideturtle()
            screen.onkey(None, "1")
            screen.onkey(None, "2")
            screen.onkey(None, "3")
            screen.onkey(None, "4")
            screen.onkey(None, "5")
            screen.onkey(None, "6")
            screen.onkey(None, "7")
            screen.onkey(None, "8")
            screen.onkey(None, "9")
            screen.onkey(None, "0")

            y = float(9)

            cal_helper2.hideturtle()
            cal_helper2.pen(speed=125)
            cal_helper2.right(-90)
            cal_helper2.penup()
            cal_helper2.forward(216)
            cal_helper2.right(90)
            cal_helper2.forward(93)
            cal_helper2.color("white")
            cal_helper2.write(f"{y}", True, align="right",
                              font=("Gothic Century", 30))
            secondnum = "1"

        def second0():
            cal_helper1.reset()
            cal_helper1.hideturtle()
            screen.onkey(None, "1")
            screen.onkey(None, "2")
            screen.onkey(None, "3")
            screen.onkey(None, "4")
            screen.onkey(None, "5")
            screen.onkey(None, "6")
            screen.onkey(None, "7")
            screen.onkey(None, "8")
            screen.onkey(None, "9")
            screen.onkey(None, "0")

            y = float(0)

            cal_helper2.hideturtle()
            cal_helper2.pen(speed=125)
            cal_helper2.right(-90)
            cal_helper2.penup()
            cal_helper2.forward(216)
            cal_helper2.right(90)
            cal_helper2.forward(93)
            cal_helper2.color("white")
            cal_helper2.write(f"{y}", True, align="right",
                              font=("Gothic Century", 30))
            secondnum = "1"

        screen.onkey(second1, "1")
        screen.onkey(second2, "2")
        screen.onkey(second3, "3")
        screen.onkey(second4, "4")
        screen.onkey(second5, "5")
        screen.onkey(second6, "6")
        screen.onkey(second7, "7")
        screen.onkey(second8, "8")
        screen.onkey(second9, "9")
        screen.onkey(second0, "0")

        def negnum2():

            def neg1():
                cal_helper1.reset()
                cal_helper1.hideturtle()
                y = float(-1)

                screen.onkey(None, "1")
                screen.onkey(None, "2")
                screen.onkey(None, "3")
                screen.onkey(None, "4")
                screen.onkey(None, "5")
                screen.onkey(None, "6")
                screen.onkey(None, "7")
                screen.onkey(None, "8")
                screen.onkey(None, "9")
                screen.onkey(None, "0")

                cal_helper2.hideturtle()
                cal_helper2.pen(speed=125)
                cal_helper2.right(-90)
                cal_helper2.penup()
                cal_helper2.forward(216)
                cal_helper2.right(90)
                cal_helper2.forward(93)
                cal_helper2.color("white")
                cal_helper2.write(f"{y}", True, align="right",
                                  font=("Gothic Century", 30))

            def neg2():
                cal_helper1.reset()
                cal_helper1.hideturtle()
                y = float(-2)

                cal_helper2.hideturtle()
                cal_helper2.pen(speed=125)
                cal_helper2.right(-90)
                cal_helper2.penup()
                cal_helper2.forward(216)
                cal_helper2.right(90)
                cal_helper2.forward(93)
                cal_helper2.color("white")
                cal_helper2.write(f"{y}", True, align="right",
                                  font=("Gothic Century", 30))

            def neg3():
                cal_helper1.reset()
                cal_helper1.hideturtle()
                y = float(-3)

                cal_helper2.hideturtle()
                cal_helper2.pen(speed=125)
                cal_helper2.right(-90)
                cal_helper2.penup()
                cal_helper2.forward(216)
                cal_helper2.right(90)
                cal_helper2.forward(93)
                cal_helper2.color("white")
                cal_helper2.write(f"{y}", True, align="right",
                                  font=("Gothic Century", 30))

            def neg4():
                cal_helper1.reset()
                cal_helper1.hideturtle()
                y = float(-4)

                cal_helper2.hideturtle()
                cal_helper2.pen(speed=125)
                cal_helper2.right(-90)
                cal_helper2.penup()
                cal_helper2.forward(216)
                cal_helper2.right(90)
                cal_helper2.forward(93)
                cal_helper2.color("white")
                cal_helper2.write(f"{y}", True, align="right",
                                  font=("Gothic Century", 30))

            def neg5():
                cal_helper1.reset()
                cal_helper1.hideturtle()
                y = float(-5)

                cal_helper2.hideturtle()
                cal_helper2.pen(speed=125)
                cal_helper2.right(-90)
                cal_helper2.penup()
                cal_helper2.forward(216)
                cal_helper2.right(90)
                cal_helper2.forward(93)
                cal_helper2.color("white")
                cal_helper2.write(f"{y}", True, align="right",
                                  font=("Gothic Century", 30))

            def neg6():
                cal_helper1.reset()
                cal_helper1.hideturtle()
                y = float(-6)

                cal_helper2.hideturtle()
                cal_helper2.pen(speed=125)
                cal_helper2.right(-90)
                cal_helper2.penup()
                cal_helper2.forward(216)
                cal_helper2.right(90)
                cal_helper2.forward(93)
                cal_helper2.color("white")
                cal_helper2.write(f"{y}", True, align="right",
                                  font=("Gothic Century", 30))

            def neg7():
                cal_helper1.clear()
                y = float(-7)

                cal_helper2.hideturtle()
                cal_helper2.pen(speed=125)
                cal_helper2.right(-90)
                cal_helper2.penup()
                cal_helper2.forward(216)
                cal_helper2.right(90)
                cal_helper2.forward(93)
                cal_helper2.color("white")
                cal_helper2.write(f"{y}", True, align="right",
                                  font=("Gothic Century", 30))

            def neg8():
                cal_helper1.reset()
                cal_helper1.hideturtle()
                y = float(-8)

                cal_helper2.hideturtle()
                cal_helper2.pen(speed=125)
                cal_helper2.right(-90)
                cal_helper2.penup()
                cal_helper2.forward(216)
                cal_helper2.right(90)
                cal_helper2.forward(93)
                cal_helper2.color("white")
                cal_helper2.write(f"{y}", True, align="right",
                                  font=("Gothic Century", 30))

            def neg9():
                cal_helper1.reset()
                cal_helper1.hideturtle()
                y = float(-9)

                cal_helper2.hideturtle()
                cal_helper2.pen(speed=125)
                cal_helper2.right(-90)
                cal_helper2.penup()
                cal_helper2.forward(216)
                cal_helper2.right(90)
                cal_helper2.forward(93)
                cal_helper2.color("white")
                cal_helper2.write(f"{y}", True, align="right",
                                  font=("Gothic Century", 30))

            def neg0():
                cal_helper1.reset()
                cal_helper1.hideturtle()
                y = float(0)

                cal_helper2.hideturtle()
                cal_helper2.pen(speed=125)
                cal_helper2.right(-90)
                cal_helper2.penup()
                cal_helper2.forward(216)
                cal_helper2.right(90)
                cal_helper2.forward(93)
                cal_helper2.color("white")
                cal_helper2.write(f"{y}", True, align="right",
                                  font=("Gothic Century", 30))

            screen.onkey(neg1, "1")
            screen.onkey(neg2, "2")
            screen.onkey(neg3, "3")
            screen.onkey(neg4, "4")
            screen.onkey(neg5, "5")
            screen.onkey(neg6, "6")
            screen.onkey(neg7, "7")
            screen.onkey(neg8, "8")
            screen.onkey(neg9, "9")
            screen.onkey(neg0, "0")

        if float(y) < float(0):
            screen.onkey(None, "1")
            screen.onkey(None, "2")
            screen.onkey(None, "3")
            screen.onkey(None, "4")
            screen.onkey(None, "5")
            screen.onkey(None, "6")
            screen.onkey(None, "7")
            screen.onkey(None, "8")
            screen.onkey(None, "9")
            screen.onkey(None, "0")

            time.sleep(1)
            secondnum = "1"

        if float(y) >= float(0):
            screen.onkey(None, "1")
            screen.onkey(None, "2")
            screen.onkey(None, "3")
            screen.onkey(None, "4")
            screen.onkey(None, "5")
            screen.onkey(None, "6")
            screen.onkey(None, "7")
            screen.onkey(None, "8")
            screen.onkey(None, "9")
            screen.onkey(None, "0")

            time.sleep(1)
            secondnum = "1"

        screen.onkey(negnum2, "n")

    turtle.ontimer(check2, 5000)


def k():
    print("")


screen.listen()

# Screen stuff
Windows_10 = turtle.Screen()
# Windows_10.register_shape('intro_ball.gif')

# Computer shape
start = turtle.setup(width=.99, height=0.9, startx=None, starty=None)
start = turtle.title("Your Computer - Windows 10")
start = turtle.Turtle()
start.position()
start.pen(speed=125)
start.forward(100)
start.backward(365)
start.right(-90)
start.forward(285)
start.right(90)
start.forward(525)
start.right(90)
start.forward(285)
start.right(90)
start.forward(175)
start.forward(130)
start.right(-90)
start.forward(75)
start.right(-90)
start.forward(80)
start.right(-90)
start.forward(75)
start.penup()
start.right(180)
start.forward(75)
start.right(-90)
start.pendown()
start.forward(75)
start.right(90)
start.forward(75)
start.right(90)
start.forward(225)
start.right(90)
start.forward(75)
start.right(90)
start.forward(100)
start.hideturtle()
#screen.textinput("Hello!", "Welcome to your new computer")
# start.shape("intro_ball.gif")

# Background Coloring
bg = turtle.Turtle()
bg.pen(speed=15)
bg.penup()
bg.right(-90)
bg.forward(25)
bg.right(-90)
bg.forward(264)
bg.right(-90)
bg.right(-90)
bg.fillcolor(bg_col)
bg.begin_fill()
for _ in range(4):
    bg.forward(259)
    bg.right(-90)

bg.end_fill()
bg.forward(259)
bg.begin_fill()
for _ in range(4):
    bg.forward(259)
    bg.right(-90)

bg.end_fill()
bg.forward(215)
bg.begin_fill()
for _ in range(4):
    bg.forward(50)
    bg.right(-90)

bg.end_fill()
bg.right(-90)
bg.forward(55)
bg.right(90)
bg.forward(25)

bg.begin_fill()
for _ in range(4):
    bg.forward(25)
    bg.right(-90)

bg.end_fill()
bg.right(90)
bg.forward(-1)
bg.begin_fill()
for _ in range(4):
    bg.forward(25)
    bg.right(-90)

bg.end_fill()
bg.backward(48)
bg.begin_fill()
for _ in range(4):
    bg.forward(25)
    bg.right(-90)

bg.end_fill()
bg.backward(25)
bg.begin_fill()
for _ in range(4):
    bg.forward(25)
    bg.right(-90)

bg.end_fill()
bg.backward(25)
bg.begin_fill()
for _ in range(4):
    bg.forward(25)
    bg.right(-90)

bg.end_fill()
bg.backward(25)
bg.begin_fill()
for _ in range(4):
    bg.forward(25)
    bg.right(-90)

bg.end_fill()
bg.backward(25)
bg.begin_fill()
for _ in range(4):
    bg.forward(25)
    bg.right(-90)

bg.end_fill()
bg.backward(25)
bg.begin_fill()
for _ in range(4):
    bg.forward(25)
    bg.right(-90)

bg.end_fill()
bg.backward(25)
bg.begin_fill()
for _ in range(4):
    bg.forward(25)
    bg.right(-90)

bg.end_fill()
bg.backward(5)
bg.begin_fill()
for _ in range(4):
    bg.forward(25)
    bg.right(-90)

bg.end_fill()
bg.hideturtle()

# Calculator code
calc = turtle.Turtle()
calc.hideturtle()
calc.pen(speed=125)
calc.penup()
calc.right(-90)
calc.forward(200)
calc.right(-90)
calc.forward(250)
calc.right(90)
calc.pendown()
calc.forward(75)
calc.right(90)
calc.forward(65)
calc.right(90)
calc.forward(75)
calc.right(90)
calc.forward(65)
calc.penup()
calc.backward(7)
calc.right(90)
calc.forward(55)
calc.pendown()
calc.forward(15)
calc.right(90)
calc.forward(52)
calc.right(90)
calc.forward(15)
calc.right(90)
calc.forward(52)
calc.right(-90)
calc.penup()
calc.forward(10)
calc.right(-180)
calc.pendown()
calc.forward(7)
calc.right(90)
calc.forward(15)
calc.right(90)
calc.forward(7)
calc.right(90)
calc.forward(15)
calc.penup()
calc.backward(18)
calc.right(90)
calc.pendown()
calc.forward(7)
calc.right(90)
calc.forward(15)
calc.right(90)
calc.forward(7)
calc.right(90)
calc.forward(15)
calc.penup()
calc.backward(18)
calc.right(90)
calc.pendown()
calc.forward(7)
calc.right(90)
calc.forward(15)
calc.right(90)
calc.forward(7)
calc.right(90)
calc.forward(15)
calc.penup()
calc.right(-90)
calc.forward(3)
calc.right(90)
calc.forward(36)
calc.pendown()
calc.right(-90)
calc.forward(7)
calc.right(-90)
calc.forward(15)
calc.right(-90)
calc.forward(7)
calc.right(-90)
calc.forward(15)
calc.penup()
calc.backward(18)
calc.right(-90)
calc.pendown()
calc.forward(7)
calc.right(-90)
calc.forward(15)
calc.right(-90)
calc.forward(7)
calc.right(-90)
calc.forward(15)
calc.penup()
calc.backward(18)
calc.right(-90)
calc.pendown()
calc.forward(7)
calc.right(-90)
calc.forward(15)
calc.right(-90)
calc.forward(7)
calc.right(-90)
calc.forward(15)
calc.penup()
calc.right(-90)
calc.forward(17)
calc.right(90)
calc.forward(36)
calc.right(90)
calc.pendown()
calc.forward(7)
calc.right(90)
calc.forward(15)
calc.right(90)
calc.forward(7)
calc.right(90)
calc.forward(15)
calc.penup()
calc.backward(18)
calc.pendown()
calc.right(90)
calc.forward(7)
calc.right(90)
calc.forward(15)
calc.right(90)
calc.forward(7)
calc.right(90)
calc.forward(15)
calc.penup()
calc.backward(18)
calc.pendown()
calc.right(90)
calc.forward(7)
calc.right(90)
calc.forward(15)
calc.right(90)
calc.forward(7)
calc.right(90)
calc.forward(15)
calc.penup()
calc.right(-90)
calc.forward(10)
calc.right(90)
calc.forward(36)
calc.pendown()
calc.right(90)
calc.forward(7)
calc.right(90)
calc.forward(15)
calc.right(90)
calc.forward(7)
calc.right(90)
calc.forward(15)
calc.penup()
calc.backward(18)
calc.pendown()
calc.right(90)
calc.forward(7)
calc.right(90)
calc.forward(15)
calc.right(90)
calc.forward(7)
calc.right(90)
calc.forward(15)
calc.penup()
calc.backward(18)
calc.pendown()
calc.right(90)
calc.forward(7)
calc.right(90)
calc.forward(15)
calc.right(90)
calc.forward(7)
calc.right(90)
calc.forward(15)
calc.penup()
calc.right(-90)
calc.forward(10)
calc.right(90)
calc.forward(36)
calc.pendown()
calc.right(90)
calc.forward(7)
calc.right(90)
calc.forward(15)
calc.right(90)
calc.forward(7)
calc.right(90)
calc.forward(15)
calc.penup()
calc.backward(18)
calc.pendown()
calc.right(90)
calc.forward(7)
calc.right(90)
calc.forward(15)
calc.right(90)
calc.forward(7)
calc.right(90)
calc.forward(15)
calc.penup()
calc.backward(18)
calc.pendown()
calc.right(90)
calc.forward(7)
calc.right(90)
calc.forward(15)
calc.right(90)
calc.forward(7)
calc.right(90)
calc.forward(15)
calc.penup()
calc.right(-90)
calc.forward(20)
calc.right(90)
calc.forward(10)
calc.color("white")
calc.write("Calculator", False, align="center")
screen.onkey(c, "c")

sw = turtle.Turtle()
sw.pen(speed=125)
sw.right(-90)
sw.penup()
sw.forward(150)
sw.right(-90)
sw.forward(175)
# screen.textinput("NIM", "Name of first player:") pop-up window for text

# screen.numinput("Poker", "Your stakes:", 1000, minval=10, maxval=10000) numbers in pop-up window

# Computer task bar, based off of windows 10
comp_bar = turtle.Turtle()
comp_bar.penup()
comp_bar.pen(speed=125)
comp_bar.forward(260)
comp_bar.right(-90)
comp_bar.forward(25)
comp_bar.right(-90)
comp_bar.pendown()
comp_bar.forward(525)
comp_bar.penup()
comp_bar.right(-90)
comp_bar.forward(13)
comp_bar.right(-90)
comp_bar.forward(475)
comp_bar.hideturtle()

# Computer bar background color
comp_bar_bg = turtle.Turtle()
comp_bar_bg.pen(speed=125)
comp_bar_bg.penup()
comp_bar_bg.right(90)
comp_bar_bg.right(90)
comp_bar_bg.forward(240)
comp_bar_bg.fillcolor(comp_bar_col)
comp_bar_bg.begin_fill()
for _ in range(2):
    comp_bar_bg.forward(24)
    comp_bar_bg.right(90)
    comp_bar_bg.forward(24)
    comp_bar_bg.right(90)
    comp_bar_bg.forward(500)

comp_bar_bg.end_fill()
comp_bar_bg.hideturtle()

# The clock in the corner, adjusted for EST
sec = datetime.now(pytz.timezone('US/Eastern')).second
min = datetime.now(pytz.timezone('US/Eastern')).minute
hr = datetime.now(pytz.timezone('US/Eastern')).hour

clock = turtle.Turtle()
clock.pen(speed=5)
clock.penup()
clock.right(-90)
clock.forward(3)
clock.right(90)
clock.forward(175)
clock.pendown()
clock.hideturtle()

while True:
    clock.hideturtle()
    clock.clear()
    # display the time
    clock.color("white")
    clock.write(str(hr).zfill(2) + ":" + str(min).zfill(2) + ":" +
                str(sec).zfill(2),
                font=("Marlett", 12, "bold"))
    time.sleep(1)
    sec += 1

    if sec == 60:
        sec = 0
        min += 1

    if min == 60:
        min = 0
        hr += 1

    if hr == 13:
        hr = 1

# Looping the program so it never ends.
Screen.mainloop()

# Test stuff, misc.
test = turtle.Turtle()
test = test.goto(400, 500)
test = test.clear()

# comp = calc.write("Home = ", True, align="center")
# Writes text on screen
