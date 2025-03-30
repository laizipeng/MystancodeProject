"""
File: Steeplechase.py
Name: Brian
---------------------------------
TODO:
"""

from karel.stanfordkarel import *

def jump():
    """
    pre-condition:Karel is on the left side of the wall,facing East.
    post-condition:Karel is on the right side of the wall.
    """
    up()
    cross()
    down()


def turn_right():
    turn_left()
    turn_left()
    turn_left()
def up():
    """
    pre-condition:Karel is on the left side of the wall,facing East.
    post-condition:Karel is on the upper left of the wall.
    """
    while not front_is_clear():
        turn_left()
        move()
        turn_right()
def cross():
    move()
    turn_right()
def down():
    """
    pre-condition:Karel is at the upper right,facing South.
    post-condition:
    """
    while front_is_clear():
        move()
    turn_left()
def jump():
    up()
    cross()
    down()



def main():
    """
    Karel crosses hurdles in a 12x12 world
    with a for loop 
    """
    for i in range(11):
        if front_is_clear():
            move()
        else:
            jump()









# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    execute_karel_task(main)
