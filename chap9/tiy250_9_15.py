from random import randint, choice
import string
string.ascii_letters ='abc'


def random_fours():
    list_numbers = []
    """Create a loop to get 10 numbers and store to list random_numbers"""
    for create_number in range(10):
        selected_number = randint(1, 5)
        """If number already in list, pass and get another number"""
        if selected_number not in list_numbers:
            list_numbers.append(selected_number)

    list_letters = []
    """Create a loop to get 5 letters and store to list numbers_letters"""
    for letter in range(5):
        selected_letter = choice(string.ascii_letters.lower())
        """If letter already in list, pass and get another letter"""
        if selected_letter not in list_letters:
            list_letters.append(selected_letter.lower())

    random_list = []
    create_list = list_numbers + list_letters
    while len(random_list) < 4:
        four_numbers = choice(create_list)
        """Avoid duplicates"""
        if four_numbers not in random_list:
            random_list.append(four_numbers)

    return random_list


def create_winning_list():
    """Create empty lists to store in a list of 10 numbers and 5 letters"""
    winning_numbers_letters = random_fours()
    """Print list of 10 numbers and 5 letters"""
    return winning_numbers_letters


def random_ticket():
    """Create a random ticket"""
    my_ticket = random_fours()
    print(f"Your ticket reads: {my_ticket}")
    return my_ticket


def check_ticket(this_ticket, winning_ticket):
    for element in this_ticket:
        if element not in winning_ticket:
            return False
    return True


winning_numbers = create_winning_list()
print(f"The winning numbers are: {winning_numbers}")
ticket = random_ticket()
games_played = 0
max_games = 100000
check_ticket(ticket, winning_numbers)

while check_ticket:
    games_played += 1
    if games_played < max_games:
        new_ticket = random_fours()
        print(f"Your new ticket numbers are: {new_ticket} - so far {games_played} games played")
    else:
        break
else:
    print(f"You won the lotto, it took {games_played} games to win!")

print(f"\n\nPlayed for {games_played} without a win!")



