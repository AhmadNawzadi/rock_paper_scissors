import random


def rock_paper_scissors():
        # Rock
    rock = ("""
        _______
    ---'   ____)
        (_____)
        (_____)
        (____)
    ---.__(___)
    """)

        # Paper
    paper = ("""
        _______
    ---'    ____)____
            ______)
            _______)
            _______)
    ---.__________)
    """)

        # Scissors
    scissors = ("""
        _______
    ---'   ____)____
            ______)
        __________)
        (____)
    ---.__(___)
    """)

    rock_paper_scissors = [rock, paper, scissors]
    rock_paper_scissors_str = ['Rock', 'Paper', 'Scissors']

    print("Welcome to the Rock Paper Scissors game!")

    #USER CHOICE
    user_choice = input("Select 0 for Rock, 1 for Paper and 2 for Scissors!\n")
    int_user_choice = int(user_choice)
    if int_user_choice > 2:
        print("You typed an invalid number. You lose!")
        exit()
    user_random_RPS_text = rock_paper_scissors_str[int_user_choice]
    user_random_RPS_ACSSI_art = rock_paper_scissors[int_user_choice]
    print(f"Your choice is: {user_random_RPS_text}")
    print(user_random_RPS_ACSSI_art)

    #COMPUTER CHOICE
    computer_random_choice = random.randint(0,2)
    computer_choice_ACSSI_art = rock_paper_scissors[computer_random_choice]
    computer_random_RPS_text = rock_paper_scissors_str[computer_random_choice]
    print(f"Computer choice is: {computer_random_RPS_text}")
    print(computer_choice_ACSSI_art)
    if int_user_choice == computer_random_choice:
        print("Equal result, Game Draw!")
    elif user_random_RPS_text == "Rock" and computer_random_RPS_text == "Paper":
        print("You lose!!")
    elif user_random_RPS_text == "Paper" and computer_random_RPS_text == "Rock":
        print("You wins!")
    elif user_random_RPS_text == "Scissors" and computer_random_RPS_text == "Rock":
        print("You lose!!")
    elif user_random_RPS_text == "Scissors" and computer_random_RPS_text == "Paper":
        print("You wins!")
    elif user_random_RPS_text == "Paper" and computer_random_RPS_text == "Scissors":
        print("You lose!!")
    elif user_random_RPS_text == "Rock" and computer_random_RPS_text == "Scissors":
        print("You wins!")


if __name__ == "__main__":
    rock_paper_scissors()

    