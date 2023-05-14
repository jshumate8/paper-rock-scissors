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
import random
player1 = int(input("Type 1 for Paper, 2 for Rock, or 3 for Scissors.\n"))


prs = [paper, rock, scissors]

userprs = prs[player1-1]

comprs = random.choice(prs)

print(f"You chose:\n{userprs}")
print("\n")
print(f"Computer chose:\n{comprs}")

if userprs == comprs:
  print("It's a tie!")
elif (userprs == prs[0] and comprs == prs[2]) or (userprs == prs[1] and comprs == prs[0]) or (userprs == prs[2] and comprs == prs[1]):
  print("Computer Wins!")
else:
  print("Congratulation, You Win!")


