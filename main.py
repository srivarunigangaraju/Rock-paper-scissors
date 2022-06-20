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
import random
#Write your code below this line 👇
print("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.")
p1 = int(input())
c = random.randint(0,2)
if p1 == 0:
  if c == 1:
    print('You Lose')
  elif c == 2:
    print('You Win')
  else:
    print('Game draw')
elif p1 == 1:
  if c == 1:
    print('Game draw! try again')
  elif c == 2:
    print('you lose')
  else:
    print('You win')
else:
  if c == 2:
    print('Game draw')
  elif c == 1:
    print('You lose')
  else:
    print('you lose')