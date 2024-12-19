import tkinter as tk
from tkinter import messagebox

# Quiz data
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

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz Game")
        
        self.current_question = 0
        self.score = 0
        self.questions = list(quiz_data.keys())
        self.answers = [None] * len(self.questions)  # Track user answers (None = unanswered)
        
        # Question label
        self.question_label = tk.Label(root, text="", font=("Arial", 16), wraplength=400, justify="center")
        self.question_label.pack(pady=20)
        
        # Answer buttons
        self.answer_buttons = []
        for i in range(4):
            btn = tk.Button(root, text="", font=("Arial", 14), width=20, command=lambda idx=i: self.check_answer(idx))
            btn.pack(pady=5)
            self.answer_buttons.append(btn)
        
        # Navigation buttons
        self.button_frame = tk.Frame(root)
        self.button_frame.pack(pady=20)
        
        self.previous_button = tk.Button(self.button_frame, text="Previous Question", font=("Arial", 14), state="disabled", command=self.previous_question)
        self.previous_button.pack(side="left", padx=10)
        
        self.next_button = tk.Button(self.button_frame, text="Next Question", font=("Arial", 14), state="disabled", command=self.next_question)
        self.next_button.pack(side="left", padx=10)
        
        self.skip_button = tk.Button(self.button_frame, text="Skip Question", font=("Arial", 14), command=self.skip_question)
        self.skip_button.pack(side="left", padx=10)
        
        # Start quiz
        self.load_question()
    
    def load_question(self):
        """Load the current question and answers."""
        question = self.questions[self.current_question]
        data = quiz_data[question]
        
        self.question_label.config(text=question)
        for i, answer in enumerate(data['answers']):
            # Set button text
            self.answer_buttons[i].config(
                text=answer,
                state="normal",
                bg="green" if self.answers[self.current_question] == answer else "SystemButtonFace"
            )
        
        # Update navigation button states
        self.previous_button.config(state="normal" if self.current_question > 0 else "disabled")
        self.next_button.config(state="normal" if self.answers[self.current_question] is not None else "disabled")
        self.skip_button.config(state="normal")
    
    def check_answer(self, idx):
        """Check if the selected answer is correct and update button colors."""
        question = self.questions[self.current_question]
        correct_answer = quiz_data[question]['correct']
        selected_answer = quiz_data[question]['answers'][idx]
        
        # Highlight buttons
        if selected_answer == correct_answer:
            self.answer_buttons[idx].config(bg="green")
            if self.answers[self.current_question] is None:
                self.score += 1
        else:
            self.answer_buttons[idx].config(bg="red")
            correct_idx = quiz_data[question]['answers'].index(correct_answer)
            self.answer_buttons[correct_idx].config(bg="green")
        
        self.answers[self.current_question] = selected_answer  # Record user's answer
        
        # Disable all answer buttons
        for btn in self.answer_buttons:
            btn.config(state="disabled")
        
        self.next_button.config(state="normal")
        self.skip_button.config(state="disabled")
    
    def next_question(self):
        """Load the next question or show the end options."""
        self.current_question += 1
        if self.current_question < len(self.questions):
            self.load_question()
        else:
            self.end_options()
    
    def previous_question(self):
        """Go back to the previous question."""
        if self.current_question > 0:
            self.current_question -= 1
            self.load_question()
    
    def skip_question(self):
        """Skip the current question and move to the next."""
        self.current_question += 1
        if self.current_question < len(self.questions):
            self.load_question()
        else:
            self.end_options()
    
    def end_options(self):
        """Ask the user what to do at the end of the quiz."""
        skipped_questions = [i for i, ans in enumerate(self.answers) if ans is None]
        
        if skipped_questions:
            choice = messagebox.askyesno(
                "Quiz Completed",
                f"You have skipped {len(skipped_questions)} question(s). Do you want to review them?"
            )
            if choice:
                self.current_question = skipped_questions[0]
                self.load_question()
                return
        
        self.show_final_score()
    
    def show_final_score(self):
        """Display the final score and end the quiz."""
        messagebox.showinfo("Quiz Completed", f"Your final score is: {self.score}/{len(self.questions)}")
        self.root.quit()

# Create the GUI application
if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()


    