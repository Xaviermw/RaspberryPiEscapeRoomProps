import vlc
import RPi.GPIO as GPIO
import time
import os
import numpy as np

class Bop_It_Puzzle:
    def __init__(self, correct_sequence):
        self.stage = 1
        self.correct_sequence = correct_sequence
    def next_stage(self):
        self.stage = self.stage + 1
    def reset_stage(self):
        self.stage = 1
    def correct_stage_bop_it(self):
        return self.correct_sequence[self.stage-1]

#Set GPIO pin format
GPIO.setmode(GPIO.BCM)

GPIO.setwarnings(False)

#Set GPIO Assignments
gpio_to_bop_it = {
    "Flick It" : 17,
    "Spin It" : 27,
    "Twist It" : 22,
    "Pull It" : 23,
    "Bop It" : 25
}

magnet_assignment = 24

#Setup the GPIO buttons
GPIO.setup(gpio_to_bop_it["Flick It"], GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(gpio_to_bop_it["Spin It"], GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(gpio_to_bop_it["Twist It"], GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(gpio_to_bop_it["Pull It"], GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(gpio_to_bop_it["Bop It"], GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Create Bop-It Puzzle
puzzle = Bop_It_Puzzle(["Flick It", "Twist It", "Bop It", "Flick It", "Pull It", "Spin It", "Pull It", "Bop It"])

# Setup Alarm Magnet as On
GPIO.setup(magnet_assignment,GPIO.OUT)
GPIO.output(magnet_assignment,GPIO.HIGH)
magnet_on = GPIO.input(magnet_assignment)
latest_press = "Nothing"
previous_correct_press = "Nothing"

while puzzle.stage < 9:

    for piece in gpio_to_bop_it.keys():
#         print(puzzle.stage)
        if (GPIO.input(gpio_to_bop_it[piece]) == False):
            last_press = piece
#       if(True):
#         last_press = input("Piece Entered: ")
            if (puzzle.correct_stage_bop_it() == last_press):
#                 print(last_press)
                previous_correct_press = str(last_press)
                puzzle.next_stage()
            elif (last_press != previous_correct_press):
                puzzle.reset_stage()
            
GPIO.output(magnet_assignment,GPIO.LOW)
magnet_on = GPIO.input(magnet_assignment)
print("Completed Puzzle!")





####### Stupid Other Ways Of Doing it #######
#
# class Bop_It_Part:
#     def __init__(self, is_first, is_second, is_third, is_fourth, is_fifth, is_sixth, is_seventh, is_eighth):
#         self.is_first = is_first
#         self.is_second = is_second
#         self.is_third = is_third
#         self.is_fourth = is_fourth
#         self.is_fifth = is_fifth
#         self.is_sixth = is_sixth
#         self.is_seventh = is_seventh
#         self.is_eighth = is_eighth
# class Bop_It_Part:
#     def __init__(self, name, correct_in_sequence):
#         self.name = name
#         self.correct_in_sequence = correct_in_sequence
#     
#     def get_correct(stage):
#         return correct_in_sequence[stage-1]
 
# class Bop_It_Part:
#     def __init__(self, name, gpio_pin):
#         self.name = name
#         self.gpio_pin = gpio_pin
#     
#     def check_input(self):
#         return GPIO.input(self.gpio_pin)
########################################





            
