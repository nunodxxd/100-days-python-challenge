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
player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
cpu_choice = random.randint(0,2)

options = [rock,paper,scissors]

print("Player chose: " + options[player_choice])
print("CPU chose: " + options[cpu_choice])

if player_choice == cpu_choice:
    print("Draw")

if player_choice == 0:
    if cpu_choice == 1:
        print("CPU Win")
    elif cpu_choice == 2:
        print("Player Win")

if player_choice == 1:
    if cpu_choice == 0:
        print("Player Win")
    elif cpu_choice == 2:
        print("CPU Win")

if player_choice == 2:
    if cpu_choice == 0:
        print("CPU Win")
    elif cpu_choice == 1:
        print("Player Win")




