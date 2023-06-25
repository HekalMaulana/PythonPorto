import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

# Variable
rock_paper_scissors = [rock, paper, scissors]
random_num = random.randint(0, 2)

# User choose
user_choose = int(input("What do you choose? '0' for Rock, '1' for Paper, '2' for Scissors "))

# Show user choose
print("You choose\n")
print(rock_paper_scissors[user_choose])

# Computer choose
computer_choose = rock_paper_scissors[random_num]

# Show computer choose
print("Computer Choose\n")
print(computer_choose)

# Show the winner
if user_choose == 2 and random_num == 0:
    print("You Lose")
elif user_choose == 0 and random_num == 2:
    print("You Win")
elif user_choose >= 3 and user_choose < 0:
    print("Invalid Number, You Lose")
elif user_choose > random_num:
    print("You Win")
elif user_choose == random_num:
    print("Draw")
else:
    print("Computer Win")


