import random
from validate_numbers import Validate
import subprocess #to run the different files

def user_input_validation(user_input):
    # Validate if input is a digit
    if user_input.isdigit():
        return True
    else:
        print("Invalid input. Please enter a digit.")
        return False

def digit_length(num): 
    # To check the length of the digit
    if num == 0:
        return 1  # Special case for 0
    count = 0
    while num > 0:
        num //= 10  # Integer division to remove the last digit
        count += 1
    return count

def get_random_number():
    random_number = random.randint(1, 100)  # Generate a random number between 1 and 999
    print("A random number has been generated")
    print(f"Random number is : {random_number}")
    return random_number

def check_number(random_number, length_of_random_number):
    print(f"The length of the random number is {length_of_random_number}")

    attempt = 10
    validate = Validate()  # Create an instance of the Validate class

    while attempt >= 0:
        user_input = input("Enter what you think the number is: ")
        
        if user_input_validation(user_input):  # Validate input
            length_of_user_number = digit_length(int(user_input))

            # Check the number based on its length
            if length_of_random_number == 1:
                if validate.validate_single_digit(user_input, random_number, length_of_user_number, length_of_random_number):
                    exit()
            elif length_of_random_number == 2:
                if validate.validate_double_digit(user_input, random_number, length_of_user_number, length_of_random_number):
                    exit()
            elif length_of_random_number == 3:
                if validate.validate_triple_digit(user_input, random_number, length_of_user_number, length_of_random_number):
                    exit()

        attempt -= 1
        if attempt == 0:
            print(f"You lost. The correct number is {random_number}")
            break
        else:
            print(f"You have {attempt} attempts left.")

if __name__ == "__main__":
    while True:
        # Check for command-line arguments
        mode = input("Please enter mode of the game: 0 for terminal or 1 for GUI. ")
        if mode == "0":  # Terminal mode
            # Run the terminal game file
            random_number = get_random_number()
            length_of_random_number = digit_length(random_number)
            check_number(random_number, length_of_random_number)
            break
        elif mode == "1":  # GUI mode
            # Run the GUI game file
            subprocess.run(["python", "Guess_the_number_GUI.py"])
            break
            
        else:
            print("Invalid mode. Use 0 for terminal or 1 for GUI.")


