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

player = int(input("What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors.\n"))
computer = random.randint(0, 2)
if player == 0:
    print("You choose :")
    print(rock)
    
    if computer == 0:
        print("computer choose:")
        print(rock)
        print("It's a Draw")

    elif computer == 1:
        print("computer choose:")
        print(paper)
        print("You lose")

    else:
        print("computer choose:")
        print(scissors)
        print("You win")
elif player == 1:
    print("You choose :")
    print(paper)
    if computer == 0:
        print("computer choose:")
        print(rock)
        print("You win")

    elif computer == 1:
        print("computer choose:")
        print(paper)
        print("It's a Draw")

    else:
        print("computer choose:")
        print(scissors)
        print("You lose")
elif player == 2:
    print("You choose :")
    print(scissors)
    if computer == 0:
        print("computer choose:")
        print(rock)
        print("You lose")

    elif computer == 1:
        print("computer choose:")
        print(paper)
        print("You win")

    else:
        print("computer choose:")
        print(scissors)
        print("It's a draw")
else:
    print("You typed an invalid number, You lose!")



