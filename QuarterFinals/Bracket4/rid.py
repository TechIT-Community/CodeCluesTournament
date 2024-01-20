def main():
    print("Welcome to the Complex Riddle Solver!")

    # Define an array of tough riddles and answers
    riddles = [
        "I speak without a mouth and hear without ears. I have no body, but I come alive with wind. What am I?",
        "The more you take, the more you leave behind. What am I?",
        "What has keys but can't open locks?",
        "I have cities, but no houses. I have mountains, but no trees. I have water, but no fish. What am I?",
        "I am taken from a mine, and shut up in a wooden case, from which I am never released, and yet I am used by almost every person. What am I?",
    ]

    # Set the maximum number of attempts for riddles
    max_attempts = 3

    # Set the passphrase riddle and answer
    passphrase_riddle = "I am a word of letters three, add two and fewer there will be. What am I?"
    passphrase_answer = "few"

    # Ask the user for the passphrase
    print("To access the riddles, solve the following riddle:")
    print(passphrase_riddle)

    for attempt in range(1, max_attempts + 1):
        user_passphrase = input("Your answer: ")

        # Check if the user's answer to the passphrase is correct
        if user_passphrase.lower() == passphrase_answer:
            print("Passphrase accepted. Here are your riddles:")

            # Iterate through each riddle
            for index, riddle in enumerate(riddles, start=1):
                print(f"\nRiddle #{index}:")
                print(riddle)

                # Ask the user to solve the riddle
                for attempt_riddle in range(1, max_attempts + 1):
                    print(f"\nAttempt #{attempt_riddle}")
                    user_answer = input("Your answer: ")

                    # Check if the user's answer to the riddle is correct
                    if user_answer.lower() == "":
                        print("Congratulations! You solved the riddle!")
                        break  # Exit the loop if the answer is correct
                    else:
                        print("Sorry, that's not the correct answer.")
                        if attempt_riddle < max_attempts:
                            print("Try again!")
                        else:
                            print("Out of attempts. Moving to the next riddle.")

            break  # Exit the loop if the passphrase is correct

        else:
            print("Sorry, that's not the correct answer.")
            if attempt < max_attempts:
                print("Try again!")
            else:
                print("Out of attempts. Exiting the program.")

    print("Thanks for playing the Complex Riddle Solver!")

if __name__ == "__main__":
    main()
