filename = "programming_poll.txt"

while True:
    answer = input("Complete the sentence: I love programming because... \n Enter 'q' to quit\n")
    if answer != 'q':
        with open(filename, "a") as file_object:
            file_object.write(f"I love programming because {answer}.\n")
    else:
        print("Thank you for taking part in this poll!")
        break
