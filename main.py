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

# Taking input

inp = int(input("What do you choose ? 0 for Rock 1 for Paper and 2 for Scissors \n").strip())

# Randomizing print

zero = rock
one = paper
two = scissors
op2 = [zero, one, two]
ran = random.randint(0,2)
ran1 = op2[ran]



# If/Else handle


if inp == 0:
    print(rock)
    print(f"\n Computer chose : \n ")
    print(ran1)
elif inp == 1:
    print(paper)
    print(f" \n Computer chose :")
    print(ran1)
elif inp == 2:
    print(scissors) 
    print(f"\n Computer chose : \n ")
    print(ran1)
        
# Randomizing behviour

if inp == 0 and ran == 1:
    print("Paper beats rock! You lose.")
elif inp == 0 and ran == 2:
    print("Rock crushes scissors! You win.")
elif inp == 1 and ran == 0:
    print("Paper beats rock! You win.")
elif inp == 1 and ran == 2:
    print("Scissors cut paper! You lose.")
elif inp == 2 and ran == 0:
    print("Rock crushes scissors! You lose.")
elif inp == 2 and ran == 1:
    print("Rock crushes scissors! lose.")
elif inp == ran:
    print("Its a tie! Please try again.")
    
input("Press Enter to exit.")
