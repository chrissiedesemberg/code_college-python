from random import choice

lottery = [25, 44, 52, 4, 12, 7, 12, 22, 20, 35, "a", "b", "c", "d", "e"]
winning_numbers = []
for numbers in range(4):
    winning_ticket = choice(lottery)
    winning_numbers.append(winning_ticket)

print(f"\nIf your ticket has these numbers, you won the lotto! \n{winning_numbers}")
