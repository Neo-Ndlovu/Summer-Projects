import sys
import random
import string

def check_password(password):
        if len(password) < 8:
            print("Password has a length less than 8.")
            return False
        
        elif not any(char in "!@#$%^&*()" for char in password):
            print("Your password is missing a special character.")
            return False
        
        elif not any(char.isdigit() for char in password):
            print("Your password doesn't contain a number.")
            return False
        
        elif not any(char.islower() for char in password):
            print("Your password doesn't contain a lowercase letter.")
            return False
        
        elif not any(char.isupper() for char in password):
            print("Your password doesn't contain an uppercase letter.")
            return False
        else:
            return True


def create_password(length=10):
    if length < 8:
        print("Password must be at least 8 characters long")
        return
    
    # Define possible characters for the password
    all_characters = string.ascii_letters + string.digits + "!@#$%^&*()"
    
    # Generate password
    password = ''.join(random.choice(all_characters) for _ in range(length))
    
    print(f"Generated password: {password}")

if __name__=="__main__":
    
    input = sys.argv[1]
    input_password = sys.argv[2]

    if input == "Check":
        if check_password(input_password) is True:
            print("Password is secure.")
        else:
            print("Password is not secure; see the above error message to modify your password.")
    elif input == "Create":
        create_password(int(input_password)) #Use it as length of password being created
    else:
        print("Kindly choose between the two options: Check / Create.")
    

