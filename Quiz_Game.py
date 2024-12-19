import subprocess #to run the different files

#Questions and answers are defined using a dictionary
quiz_data = {
    "What is the capital of France?": {
        "answers": ["Berlin", "Madrid", "Paris", "Rome"],
        "correct": "Paris"  
    },
    "Which planet is known as the Red Planet?": {
        "answers": ["Earth", "Mars", "Jupiter", "Saturn"],
        "correct": "Mars"
    },
    "How many bones are there in the adult human body?" : {
        "answers": ["186", "206", "226", "246"],
        "correct": "206"
    },
    "Which breed of dog is known for its excellent sense of smell and tracking abilities?" : {
        "answers": ["Golden Retriever", "German Shepherd", "Bloodhound", "Bulldog"],
        "correct": "Bloodhound"
    },
    "What part of the brain is responsible for memory and learning?" : {
        "answers": ["Cerebellum", "Hypothalamus", "Hippocampus", "Medulla oblongata"],
        "correct": "Hippocampus"
    },
    "What is the medical term for high blood pressure?": {
        "answers": ["Hypotension", "Hypertension", "Hyperglycemia", "Acidosis"],
        "correct": "Hypertension"
    },
    "What is the title of the first Harry Potter book in the UK?": {
        "answers": ["Harry Potter and the Chamber of Secrets", "Harry Potter and the Philosopher's Stone", "Harry Potter and the Sorcerer’s Stone", "Harry Potter and the Prisoner of Azkaban" ],
        "correct": "Harry Potter and the Philosopher's Stone"
    },
    "Which animal is considered the largest living terrestrial animal?": {
        "answers": ["Giraffe", "Elephant", "Rhino", "Hippo"],
        "correct": "Elephant"
    },
    "What is the primary function of the cerebellum?": {
        "answers": ["Memory storage", "Sensory processing", "Coordination and balance", "Emotional regulation"],
        "correct": "Coordination and balance "
    },
    "Which country is Mount Everest located in?": {
        "answers": ["China", "Nepal", "India", "Bhutan"],
        "correct": "Nepal"
    },
    "In which continent is the Sahara Desert located?": {
        "answers": ["Asia", "Australia", "South America", "Africa"],
        "correct": "Africa"
    },
    "Which country has the most natural lakes in the world?": {
        "answers": ["Canada", "Finland", "Russia", "United States"],
        "correct": "Canada"
    },
    "What is the term for the deception of the mind's perception of a stimuli?" : {
        "answers": ["Delusion", "Hallucination", "Illusion", "Insight"],
        "correct": "Illusion"
    },
    "What is the largest lake in the world?" : {
        "answers": ["Caspian Sea", "Baikal", "Lake Superior", "Ontario"],
        "correct": "Baikal"
    },
    "What gas is used to extinguish fires?" : {
        "answers": ["Oxygen", "Carbon dioxide", "Hydrogen", "Nitrogen"],
        "correct": "Nitrogen"
    },
    "What animal is the national symbol of Australia?" : {
        "answers": ["Kangaroo", "Koala", "Emu", "Crocodile"],
        "correct": "Kangaroo"
    },
    "Which of the following planets is not a gas giant?" : {
        "answers": ["Jupiter", "Saturn", "Mars", "Uranus"],
        "correct": "Mars"
    }, 
    "What chemical element is designated as “Hg”?": {
        "answers": ["Silver", "Mercury", "Copper", "Tin"],
        "correct": "Mercury"
    },
    "In what year was the first international modern Olympiad held?" : {
        "answers": ["1896", "1900", "1912", "1924"],
        "correct": "1896"
    },
    "For which of these disciplines Nobel Prize is awarded?" : {
        "answers": ["Physics, Chemistry", "Physiology", "Medicine", "All of the above"],
        "correct": "All of the above"
    },
    "What is the phobia of thunder and rain?": {
        "answers": ["Agoraphobia", "Ombrophobia", "Acrophobia", "Claustrophobia"],
        "correct": "Ombrophobia"
    },
    "What is considered the lung of the Earth?": {
        "answers": ["Amazon rainforest", "The Mississippi River", "The Sahara", "Everest"],
        "correct": "Amazon rainforest"
    }
}


def run_quiz():
    score = 0  # To tell the user their score in the end

    for question, data in quiz_data.items():
        while True:  # Loop until the user provides a valid answer
            print(question)
            for i, option in enumerate(data['answers']):
                print(f"{i + 1}. {option}")
            
            user_answer = input("Please select an answer (1-4): ")
            
            # Check if the input is valid
            if user_answer.isdigit():
                user_answer = int(user_answer)
                if 1 <= user_answer <= len(data['answers']):  # Ensure the input is within range
                    if data['answers'][user_answer - 1] == data['correct']:
                        print("Correct!")
                        score += 1
                    else:
                        print("Incorrect!")
                    break  # Exit the loop for the current question
                else:
                    print("Please select a valid number between 1 and 4.")
            else:
                print("Please enter a number.")

    print(f"Your final score is: {score}/{len(quiz_data)}")


if __name__=="__main__":

    while True:
        # Check for command-line arguments
        mode = input("Please enter mode of the game, 0 for terminal or 1 for GUI: ")
        if mode == "0":  # Terminal mode
            # Run the terminal game file
            run_quiz()
            break

        elif mode == "1":  # GUI mode
            # Run the GUI game file
            subprocess.run(["python", "Quiz_Game_GUI.py"])
            break
            
        else:
            print("Invalid mode. Use 0 for terminal or 1 for GUI.")

    