class Validate:
    def validate_number(self, user_input, random_number, length_of_user_number, length_of_random_number):
        # Ensure the input has the correct length
        if length_of_user_number != length_of_random_number:
            print(f"Kindly enter the correct number of digits, expected {length_of_random_number} digits.")
            return False

        # Convert user input and random number to strings for digit comparisons
        user_input = str(user_input)
        random_number = str(random_number)

        # Exact match
        if user_input == random_number:
            print("Congratulations! You have guessed the correct number.")
            return True

        # Compare the guessed number to the random number
        user_input_int = int(user_input)
        random_number_int = int(random_number)
        
        if user_input_int >= (2 * random_number_int): #two or more times bigger than random number
            print("The number you guessed is too big.")
        elif user_input_int <= (0.5 * random_number_int): #two or more times less than random number
            print("The number you guessed is too small.")
        elif user_input_int < random_number_int:
            print("The number you guessed is smaller than the target number.")
        elif user_input_int > random_number_int:
            print("The number you guessed is larger than the target number.")
        else:
            print("Invalid input. Please enter a valid number.")
            return False

        # Count digits in correct positions
        correct_count = sum(1 for i in range(length_of_user_number) if user_input[i] == random_number[i])

        # Count digits that are correct but in the wrong position
        wrong_position_count = 0
        for i in range(length_of_user_number):
            if user_input[i] != random_number[i] and user_input[i] in random_number:
                wrong_position_count += 1

        # Provide feedback on digit correctness
        print(f"{correct_count} digit(s) are correct and in the correct position.")
        if wrong_position_count > 0:
            print(f"{wrong_position_count} digit(s) are correct but in the wrong position.")
        else:
            print("No digits are correct but in the wrong position.")

        return False

    # Call the general method for validation for each number length
    def validate_single_digit(self, user_input, random_number, length_of_user_number, length_of_random_number):
        return self.validate_number(user_input, random_number, length_of_user_number, length_of_random_number)

    def validate_double_digit(self, user_input, random_number, length_of_user_number, length_of_random_number):
        return self.validate_number(user_input, random_number, length_of_user_number, length_of_random_number)

    def validate_triple_digit(self, user_input, random_number, length_of_user_number, length_of_random_number):
        return self.validate_number(user_input, random_number, length_of_user_number, length_of_random_number)


            

