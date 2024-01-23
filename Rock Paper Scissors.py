# Programming Logic:
# 1) Define variables such as :
#     cpuScore
#     playerScore
#     TieScore
# 2) Define checkforwinner functiom
# 3) define rock beats scissors, paper beats rock, scissors beat paper
# 4) Implement  logic

import random

print("Welcome To Rock Paper Scissors Python Project !!")

cpuScore = 0
playerScore = 0
TieScore = 0
possibleOptions = ["Rock", "Paper", "Scissors"]

while(playerScore != 3 and cpuScore != 3):
    while True:
        