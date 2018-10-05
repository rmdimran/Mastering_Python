
""" My Logic :
  ============

secret_word = "giraffe"
guess = ""
attempt = 0

while guess != secret_word and attempt != 3:
    guess = input("Enter your Guess : ")
    attempt += 1


if attempt == 3:
    print("You are out of attempts! You did not win.")

else:
    print("You win!")

 """

secret_word = "giraffe"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

while guess != secret_word and not(out_of_guesses):
    if guess_count < guess_limit:
        guess = input("Enter your guess : ")
        guess_count += 1

    else:
        out_of_guesses = True

if out_of_guesses:
    print("Sorry you are out of guesses. You lose!")

else:
    print("You win!")