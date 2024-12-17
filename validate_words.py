class Validate:

    def validate_3_letter_word(user_input, word):
        # Convert both inputs to uppercase for case-insensitive comparison
        user_input = user_input.upper()
        word = word.upper()

        # Check if the word is correct
        if user_input == word:
            print("You have entered the correct word. Well Done!")
            return True

        # Count the number of matching letters in the correct positions
        correct_count = sum(1 for i in range(3) if user_input[i] == word[i])

        # Count the number of correct letters in the wrong positions
        wrong_position_count = 0
        for i in range(3):
            if user_input[i] != word[i] and user_input[i] in word:
                wrong_position_count += 1
        if wrong_position_count == 0:
            pass
        else:
            print(f"{wrong_position_count} letters are in the wrong position.")

        # Provide feedback based on the number of correct letters
        if correct_count == 2:
            print("Two letters are correct! You have 1 letter left.")
        elif correct_count == 1:
            print("One letter is correct! You have 2 letters left.")
        else:
            print("The word is incorrect. Please try again.")

        return False
    

    def validate_4_letter_word(user_input, word):

        # Convert both inputs to uppercase for case-insensitive comparison
        user_input = user_input.upper()
        word = word.upper()

        # Check if the word is correct
        if user_input == word:
            print("You have entered the correct word. Well Done!")
            return True

        # Count the number of matching letters in the correct positions
        correct_count = sum(1 for i in range(4) if user_input[i] == word[i])

        # Count the number of correct letters in the wrong positions
        wrong_position_count = 0
        for i in range(3):
            if user_input[i] != word[i] and user_input[i] in word:
                wrong_position_count += 1
        if wrong_position_count == 0:
            pass
        else:
            print(f"{wrong_position_count} letters are in the wrong position.")    

        # Provide feedback based on the number of correct letters
        if correct_count == 3:
            print("Three letters are correct! You have 1 letter left.")
        elif correct_count == 2:
            print("Two letters are correct! You have 2 letters left.")
        elif correct_count == 1:
            print("One letter is correct! You have 3 letters left.")
        else:
            print("The word is incorrect. Please try again.")

        return False
    

    def validate_5_letter_word(user_input, word):

        # Ensure both inputs are uppercase for comparison
        user_input = user_input.upper()
        word = word.upper()

        # Check if the word is correct
        if user_input == word:
            print("You have entered the correct word. Well Done!")
            return True

        # Count the number of matching letters in the correct position
        correct_count = sum(1 for i in range(5) if user_input[i] == word[i])

        # Count the number of correct letters in the wrong positions
        wrong_position_count = 0
        for i in range(3):
            if user_input[i] != word[i] and user_input[i] in word:
                wrong_position_count += 1
        if wrong_position_count == 0:
            pass
        else:
            print(f"{wrong_position_count} letters are in the wrong position.")

        # Generate feedback based on the count of matching letters
        if correct_count == 4:
            print("Four letters are correct! You have 1 letter left.")
        elif correct_count == 3:
            print("Three letters are correct! You have 2 letters left.")
        elif correct_count == 2:
            print("Two letters are correct! You have 3 letters left.")
        elif correct_count == 1:
            print("One letter is correct! You have 4 letters left.")
        else:
            print("No letters are correct! You have all 5 letters left.")

        return False
    

    def validate_6_letter_word(user_input, word):
        # Convert both inputs to uppercase for case-insensitive comparison
        user_input = user_input.upper()
        word = word.upper()

        # Check if the word is correct
        if user_input == word:
            print("You have entered the correct word. Well Done!")
            return True

        # Count the number of matching letters in the correct positions
        correct_count = sum(1 for i in range(6) if user_input[i] == word[i])

        # Count the number of correct letters in the wrong positions
        wrong_position_count = 0
        for i in range(3):
            if user_input[i] != word[i] and user_input[i] in word:
                wrong_position_count += 1
        if wrong_position_count == 0:
            pass
        else:
            print(f"{wrong_position_count} letters are in the wrong position.")

        # Provide feedback based on the number of correct letters
        if correct_count == 5:
            print("Five letters are correct! You have 1 letter left.")
        elif correct_count == 4:
            print("Four letters are correct! You have 2 letters left.")
        elif correct_count == 3:
            print("Three letters are correct! You have 3 letters left.")
        elif correct_count == 2:
            print("Two letters are correct! You have 4 letters left.")
        elif correct_count == 1:
            print("One letter is correct! You have 5 letters left.")
        else:
            print("The word is incorrect. Please try again.")

        return False
    

    def validate_7_letter_word(user_input, word):

        # Convert both inputs to uppercase for case-insensitive comparison
        user_input = user_input.upper()
        word = word.upper()

        # Check if the word is correct
        if user_input == word:
            print("You have entered the correct word. Well Done!")
            return True

        # Count the number of matching letters in the correct positions
        correct_count = sum(1 for i in range(7) if user_input[i] == word[i])

        # Count the number of correct letters in the wrong positions
        wrong_position_count = 0
        for i in range(3):
            if user_input[i] != word[i] and user_input[i] in word:
                wrong_position_count += 1
        if wrong_position_count == 0:
            pass
        else:
            print(f"{wrong_position_count} letters are in the wrong position.")

        # Provide feedback based on the number of correct letters
        if correct_count == 6:
            print("Six letters are correct! You have 1 letter left.")
        elif correct_count == 5:
            print("Five letters are correct! You have 2 letters left.")
        elif correct_count == 4:
            print("Four letters are correct! You have 3 letters left.")
        elif correct_count == 3:
            print("Three letters are correct! You have 4 letters left.")
        elif correct_count == 2:
            print("Two letters are correct! You have 5 letters left.")
        elif correct_count == 1:
            print("One letter is correct! You have 6 letters left.")
        else:
            print("The word is incorrect. Please try again.")

        return False


    def validate_8_letter_word(user_input, word):

        # Convert both inputs to uppercase for case-insensitive comparison
        user_input = user_input.upper()
        word = word.upper()
        
        # Check if the word is correct
        if user_input == word:
            print("You have entered the correct word. Well Done!")
            return True

        # Count the number of matching letters in the correct positions
        correct_count = sum(1 for i in range(8) if user_input[i] == word[i])

        # Count the number of correct letters in the wrong positions
        wrong_position_count = 0
        for i in range(3):
            if user_input[i] != word[i] and user_input[i] in word:
                wrong_position_count += 1
        if wrong_position_count == 0:
            pass
        else:
            print(f"{wrong_position_count} letters are in the wrong position.")

        # Provide feedback based on the number of correct letters
        if correct_count == 7:
            print("Seven letters are correct! You have 1 letter left.")
        elif correct_count == 6:
            print("Six letters are correct! You have 2 letters left.")
        elif correct_count == 5:
            print("Five letters are correct! You have 3 letters left.")
        elif correct_count == 4:
            print("Four letters are correct! You have 4 letters left.")
        elif correct_count == 3:
            print("Three letters are correct! You have 5 letters left.")
        elif correct_count == 2:
            print("Two letters are correct! You have 6 letters left.")
        elif correct_count == 1:
            print("One letter is correct! You have 7 letters left.")
        else:
            print("The word is incorrect. Please try again.")

        return False
