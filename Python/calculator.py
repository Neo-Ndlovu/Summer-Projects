import subprocess #to run the different files

def is_number(user_input): #Validate if given input is a digit
    try:
        float(user_input)
        return True
    except ValueError:
        return False

def validate_user_input():
    operands = ["+", "-", "*", "/"]

    # Initialize variables to track user inputs
    user_input_1 = None
    user_input_2 = None
    user_input_operand = None

    while True:
        # Validate the first number
        if user_input_1 is None:
            user_input_1 = input("Kindly enter the first digit you want to perform operations on: ")
            if is_number(user_input_1) is False:
                print("Please enter a valid digit.")
                user_input_1 = None  # Reset to prompt again
                continue #Use continue to immediately ask the same question again if an invalid input is given

        # Validate the second number
        if user_input_2 is None:
            user_input_2 = input("Kindly enter the second digit you want to perform operations on: ")
            if is_number(user_input_2) is False:
                print("Please enter a valid digit.")
                user_input_2 = None  # Reset to prompt again
                continue

        # Validate the operand
        if user_input_operand is None:
            user_input_operand = input("Kindly enter the operand that you want to be performed on the two numbers you have entered: ")
            if user_input_operand not in operands:
                print("Please enter a valid operand.")
                user_input_operand = None  # Reset to prompt again
                continue

        # If all inputs are valid, return them as a tuple
        return float(user_input_1), float(user_input_2), user_input_operand


def perform_operation(user_input_1, user_input_2, user_input_operand):

    if user_input_operand == "+":
        answer = user_input_1 + user_input_2
        print(f"The answer is {answer}")

    elif user_input_operand == "-":
        answer = user_input_1 - user_input_2
        print(f"The answer is {answer}")
    
    elif user_input_operand == "*":
        answer = user_input_1 * user_input_2
        print(f"The answer is {answer}")

    elif user_input_operand == "/":
        answer = user_input_1 // user_input_2
        print(f"The answer is {answer}")
    


if __name__=="__main__":
    while True:
        # Check for command-line arguments
        mode = input("Please enter mode of the game: 0 for terminal or 1 for GUI. ")
        if mode == "0":  # Terminal mode
            # Run the terminal game file
            user_input_1, user_input_2, user_input_operand = validate_user_input()
            perform_operation(user_input_1, user_input_2, user_input_operand)
            break
        elif mode == "1":  # GUI mode
            # Run the GUI game file
            subprocess.run(["python", "calculator_GUI.py"])
            break
            
        else:
            print("Invalid mode. Use 0 for terminal or 1 for GUI.")
