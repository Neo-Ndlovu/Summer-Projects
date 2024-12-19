import tkinter as tk
from tkinter import messagebox
import random

# Function to generate a random word based on the word length
def get_random_word(word_length):
    # Predefined word lists based on length
    three_letter_word_list = ["And", "Fix", "Own", "Are", "Fly", "Odd", "Ape", "Fry", "Our", "Ace", "For", "Pet", "Act", "Got", "Pat", "Ask", "Get", "Peg",
                              "Arm", "God",	"Paw", "Age", "Gel", "Pup", "Ago", "Gas", "Pit", "Air",	"Hat", "Put", "Ate", "Hit",	"Pot", "All", "Has", "Pop", 
                              "But", "Had", "Pin", "Bye", "How", "Rat", "Bad", "Her", "Rag", "Big",	"His", "Rub", "Bed", "Hen", "Row", "Bat", "Ink", "Rug", 
                              "Boy", "Ice",	"Run", "Bus", "Ill", "Rap", "Bag", "Jab", "Ram", "Box",	"Jug", "Sow", "Bit", "Jet",	"See", "Bee", "Jam", "Saw",
                              "Buy", "Jar",	"Set", "Bun", "Job", "Sit", "Cub", "Jog", "Sir", "Cat",	"Kit", "Sat", "Car", "Key",	"Sob", "Cut", "Lot", "Tap", 
                              "Cow", "Lit",	"Tip", "Cry", "Let", "Top", "Cab", "Lay", "Tug", "Can",	"Mat", "Tow", "Dad", "Man",	"Toe", "Dab", "Mad", "Tan", 
                              "Dam", "Mug",	"Ten", "Did", "Mix", "Two", "Dug", "Map", "Use", "Den",	"Mum", "Van", "Dot", "Mud",	"Vet", "Dip", "Mom", "Was",
                              "Day", "May",	"Wet", "Ear", "Met", "Win", "Eye", "Net", "Won", "Eat",	"New", "Wig", "End", "Nap",	"War", "Elf", "Now", "Why", 
                              "Egg", "Nod",	"Who", "Far", "Net", "Way", "Fat", "Not", "Wow", "Few",	"Nut", "You", "Fan", "Oar",	"Yes", "Fun", "One", "Yak", 
                              "Fit", "Out", "Yet", "Fin", "Owl", "Zip", "Fox", "Old", "Zap"]

    four_letter_word_list = ["Bake","Word",	"List", "Four",	"Five",	"Nine", "Good",	"Best",	"Cute", "Zero",	"Huge",	"Cool", "Tree",	"Race",	"Rice", "Keep",
                            "Lace",	"Beam", "Game",	"Mars",	"Tide", "Ride",	"Hide",	"Exit", "Hope",	"Cold",	"From", "Need",	"Stay",	"Come"]

    five_letter_word_list = ["About", "Alert", "Argue",	"Beach", "Above", "Alike", "Arise",	"Began", "Abuse", "Alive", "Array",	"Begin", "Actor", "Allow",	
                             "Aside", "Begun", "Acute", "Alone", "Asset", "Being", "Admit", "Along", "Audio", "Below", "Adopt",	"Alter", "Audit", "Bench",
                             "Adult", "Among", "Avoid",	"Billy", "After", "Anger", "Award",	"Birth", "Again", "Angle", "Aware",	"Black", "Agent", "Angry",	
                             "Badly", "Blame", "Agree",	"Apart", "Baker", "Blind", "Ahead",	"Apple", "Bases", "Block", "Alarm",	"Apply", "Basic", "Blood",
                             "Album", "Arena", "Basis",	"Board", "Boost", "Buyer", "China",	"Cover", "Booth", "Cable", "Chose",	"Craft", "Bound", "Calif",	
                             "Civil", "Crash", "Debut",	"Entry", "Forth", "Group", "Delay",	"Equal", "Forty", "Grown", "Drove",	"Fifty", "Glass", "House",
                             "Dying", "Fight", "Globe",	"Human", "Earth", "Fixed", "Grade",	"Index", "Eight", "Flash", "Grand",	"Inner", "Large", "Loose",	
                             "Minus", "Noted", "Laser",	"Lower", "Mixed", "Novel", "Later",	"Lucky", "Model", "Nurse", "Laugh",	"Lunch", "Money", "Occur", 
                             "Layer", "Lying", "Month",	"Ocean", "Learn", "Magic", "Moral",	"Offer", "Lease", "Major", "Motor",	"Often", "Least", "Maker",	
                             "Mount", "Order", "Leave",	"March", "Mouse", "Other", "Shoot",	"Spoke", "Taken", "Touch", "Short",	"Sport", "Taste", "Tough", 
                             "Smoke", "Store", "Think",	"Twice", "Solid", "Storm", "Third",	"Under", "Solve", "Story", "Those",	"Undue", "Sorry", "Strip",	
                             "Three", "Union", "Sound",	"Stuck", "Threw", "Unity", "South",	"Study", "Throw", "Until", "Upper",	"Wrong", "Usual", "Train",	
                             "Wheel", "Wrote", "Valid",	"World", "Where", "Yield", "Virus",	"Worst", "White", "Worth", "Visit",	"Would", "Vital", "Voice"]

    six_letter_word_list = ["Abroad", "Casual",	"Around", "Couple", "Accept", "Caught",	"Arrive", "Course", "Access", "Centre",	"Artist", "Covers", "Across",
                            "Centum", "Aspect",	"Create", "Acting",	"Chance", "Assess",	"Credit", "Action",	"Change", "Assist",	"Crisis", "Active",	"Charge",	
                            "Assume", "Custom", "Actual", "Choice",	"Attack", "Damage", "Advice", "Choose",	"Attend", "Danger", "Advise", "Chosen",	"August",	
                            "Dealer", "Affect",	"Church", "Author",	"Debate", "Afford",	"Circle", "Avenue",	"Decade", "Afraid",	"Client", "Backed",	"Decide", 
                            "Agency", "Closed",	"Barely", "Defeat", "Agenda", "Closer",	"Battle", "Defend",	"Column", "Became",	"Degree", "Amount",	"Combat",	
                            "Become", "Demand", "Animal", "Coming",	"Before", "Depend", "Annual", "Common",	"Behalf", "Deputy", "Answer", "Comply",	"Behind",	
                            "Desert", "Beyond",	"Budget", "During",	"Device", "Bishop",	"Burden", "Easily",	"Differ", "Border",	"Bureau", "Eating",	"Dinner", 
                            "Bottle", "Button",	"Editor", "Direct", "Bottom", "Camera",	"Effect", "Doctor", "Bridge", "Career",	"Eleven", "Driven", "Bright",	
                            "Castle", "Emerge",	"Driver"]

    seven_letter_word_list = ["Ability", "Backing",	"Cabinet", "Absence", "Balance", "Calibre", "Academy", "Banking", "Calling", "Account",	"Barrier", "Capable", 
                              "Accused", "Battery",	"Capital", "Achieve", "Bearing", "Captain", "Acquire", "Beating", "Caption", "Already",	"Brought", "Channel", 
                              "Analyst", "Burning",	"Chapter", "Ancient", "Dealing", "Charity", "Another", "Decided", "Charlie", "Anxiety",	"Decline", "Charter",
                              "Anxious", "Default",	"Checked", "Anybody", "Defence", "Chicken", "Applied", "Deficit", "Chronic", "Arrange",	"Deliver", "Circuit", 
                              "Arrival", "Density",	"Classes", "Article", "Deposit", "Classic", "Assault", "Desktop", "Climate", "Assumed",	"Despite", "Closing", 
                              "Assured", "Destroy",	"Closure", "Attempt", "Develop", "Clothes", "Example", "Failing", "Confirm", "Excited",	"Failure", "Connect", 
                              "Exclude", "Fashion",	"Consent", "Exhibit", "Feature", "Consist", "Expense", "Federal", "Contact", "Explain",	"Feeling", "Contain", 
                              "Explore", "Fiction",	"Content", "Express", "Fifteen", "Contest", "Extreme", "Filling", "Context", "Gallery",	"Finance", "Control", 
                              "Gateway", "Finding",	"Convert", "General", "Fishing", "Correct", "Genetic", "Fitness", "Council", "Genuine",	"Foreign", "Counsel", 
                              "Gigabit", "Forever",	"Counter", "Hanging", "Fortune", "Crucial", "Heading", "Forward", "Crystal", "Herself",	"Imagine", "Journey", 
                              "Highway", "Imaging",	"Justice", "Himself", "Improve", "Justify", "History", "Include", "Keeping", "Holding",	"Initial", "Killing", 
                              "Holiday", "Inquiry",	"Kingdom", "Housing", "Insight", "Kitchen", "However", "Install", "Knowing", "Offence",	"Painted", "Mistake", 
                              "Officer", "Parking",	"Mixture", "Ongoing", "Partial", "Monitor", "Overall", "Penalty", "Premium", "Proudly",	"Pending", "Prepare", 
                              "Project", "Pension",	"Present", "Promise", "Pealing", "Prevent", "Promote", "Perfect", "Primary", "Quarter",	"Section", "Success", 
                              "Radical", "Segment",	"Suggest", "Railway", "Serious", "Summary", "Readily", "Service", "Support", "Reading",	"Serving", "Suppose", 
                              "Reality", "Session",	"Supreme", "Realise", "Setting", "Surface", "Require", "Somehow", "Thought", "Reserve",	"Someone", "Through", 
                              "Resolve", "Speaker",	"Tonight", "Respect", "Special", "Totally", "Respond", "Species", "Touched", "Restore",	"Sponsor", "Towards", 
                              "Retired", "Station",	"Traffic", "Revenue", "Storage", "Trouble", "Reverse", "Strange", "Turning", "Satisfy",	"Subject", "Unusual", 
                              "Science", "Succeed",	"Upgrade", "Walking", "Whether", "Upscale", "Wanting", "Willing", "Utility", "Warning",	"Winning", "Variety", 
                              "Warrant", "Without",	"Various", "Wearing", "Witness", "Vehicle", "Weather", "Working", "Venture", "Weekend",	"Whereas", "Viewing",]
    
    eight_letter_word_list = ["Absolute", "Bachelor", "Computer", "Abstract", "Bacteria", "Conclude", "Academic", "Baseball", "Concrete", "Accepted", "Bathroom", 
                              "Conflict", "Accident", "Becoming", "Constant", "Acquired", "Breeding", "Consumer", "Activity", "Building", "Continue", "Actually", 
                              "Bulletin", "Contract", "Addition", "Business", "Contrary", "Adequate", "Calendar", "Contrast", "Adjacent", "Campaign", "Convince", 
                              "Adjusted", "Capacity", "Corridor", "Advanced", "Cashmere", "Coverage", "Advisory", "Casualty", "Covering", "Advocate", "Catching", 
                              "Creation", "Affected", "Category", "Creative", "Aircraft", "Catholic", "Criminal", "Alliance", "Cautious", "Critical", "Although", 
                              "Cellular", "Crossing", "Aluminum", "Ceremony", "Cultural", "Analysis", "Chairman", "Currency", "Announce", "Champion", "Customer", 
                              "Anything", "Chemical", "Database", "Anywhere", "Children", "Daughter", "Apparent", "Circular", "Daylight", "Appendix", "Civilian", 
                              "Deadline", "Approach", "Clearing", "Deciding", "Approval", "Clinical", "Decision", "Argument", "Clothing", "Decrease", "Artistic", 
                              "Collapse", "Deferred", "Assembly", "Colonial", "Definite", "Assuming", "Colorful", "Delicate", "Athletic", "Commence", "Delivery", 
                              "Attached", "Commerce", "Comprise", "Diameter", "Doubtful", "Emerging", "Directly", "Dramatic", "Emphasis", "Director", "Dressing",
                              "Employee", "Disabled", "Dropping", "Endeavor", "Entirely", "Disorder", "Educated", "Entrance", "Disposal", "Efficacy", "Envelope", 
                              "Distance", "Eighteen", "Equality", "Distinct", "Election", "Equation", "District", "Electric", "Estimate", "Dividend", "Eligible", 
                              "Evaluate", "Division", "External", "Eventual", "Doctrine", "Facility", "Everyday", "Document", "Familiar", "Everyone", "Domestic", 
                              "Featured", "Evidence", "Dominant", "Feedback", "Exchange", "Dominate", "Festival", "Exciting", "Floating", "Finished", "Exercise", 
                              "Football", "Firewall", "Explicit", "Foothill", "Flagship", "Exposure", "Forecast", "Flexible", "Extended", "Foremost", "Function", 
                              "Guidance", "Formerly", "Generate", "Handling", "Fourteen", "Generous", "Hardware", "Fraction", "Genomics", "Included", "Initiate", 
                              "Identify", "Increase", "Innocent", "Identity", "Indicate", "Inspired", "Ideology", "Indirect", "Instance", "Intimate", "Industry", 
                              "Integral", "Intranet", "Informal", "Intended", "Invasion", "Informed", "Interact", "Junction", "Laughter", "Material", "Minority", 
                              "Learning", "Maturity", "Mobility", "Leverage", "Maximize", "Modeling", "Occasion", "Printing", "Parallel", "Offering", "Priority", 
                              "Optional", "Proposal", "Petition", "Ordinary", "Prospect", "Provider", "Pleasant", "Relevant", "Province", "Pleasure", "Reliable", 
                              "Publicly", "Politics", "Reliance", "Remember", "Quantity", "Position", "Renowned", "Question", "Positive", "Repeated", "Rational", 
                              "Possible", "Required", "Receiver", "Precious", "Research", "Recovery", "Pregnant", "Reserved", "Revision", "Schedule", "Resource", 
                              "Rigorous", "Scrutiny", "Response", "Romantic", "Seasonal", "Restrict", "Sampling", "Stunning", "Sensible", "Southern", "Suburban", 
                              "Sentence", "Speaking", "Suitable", "Separate", "Specific", "Survival", "Shoulder", "Standout", "Symbolic", "Slightly", "Strategy", 
                              "Sympathy", "Training", "Tailored", "Thinking", "Transfer", "Taxation", "Thousand", "Triangle", "Turnover", "Umbrella", "Universe", 
                              "Weakness", "Withdraw", "Unlawful", "Weighted", "Woodland", "Unlikely", "Whatever", "Workshop", "Valuable", "Victoria", "Wireless", "Violence"]
    
    # Depending on the word length passed, pick the right list
    if word_length == 3:
        word_list = three_letter_word_list
    elif word_length == 4:
        word_list = four_letter_word_list
    elif word_length == 5:
        word_list = five_letter_word_list
    elif word_length == 6:
        word_list = six_letter_word_list
    elif word_length == 7:
        word_list = seven_letter_word_list
    elif word_length == 8:
        word_list = eight_letter_word_list
    else:
        return None  # Invalid word length
    
    # Return a random word from the selected list
    return random.choice(word_list)

# Function to initialize the game
def start_game():
    global word, display_word, attempts
    word_length_str = length_entry.get()  # Get the word length from the user input

    # Check if the input is valid and within the range 3 to 6
    if word_length_str.isdigit():
        word_length = int(word_length_str)  # Convert to integer
        if word_length < 3 or word_length > 8:
            messagebox.showwarning("Invalid Length", "Please enter a word length between 3 and 8.")
            return  # Exit the function if the length is out of range
    else:
        messagebox.showwarning("Invalid Input", "Please enter a valid number between 3 and 8.")
        return  # Exit the function if the input is not a valid number

    # Get a random word based on the valid word length
    word = get_random_word(word_length).lower()
    display_word = ["_"] * len(word)  # Hide the word
    attempts = 10  # Set the number of attempts
    word_label.config(text=" ".join(display_word))
    attempts_label.config(text=f"Attempts left: {attempts}")
    guess_entry.delete(0, tk.END)
    guess_entry.focus()

# Function to handle the player's guess
def make_guess():
    global word, display_word, attempts
    guess = guess_entry.get().lower()
    
    # Check if the guess is valid
    if len(guess) != 1 or not guess.isalpha():
        messagebox.showwarning("Invalid input", "Please enter a single letter.")
        return
    
    if guess in word:
        # Update the display_word with correct guesses
        for i, letter in enumerate(word):
            if letter == guess:
                display_word[i] = guess
        word_label.config(text=" ".join(display_word))
    else:
        # Decrease the number of attempts if guess is incorrect
        attempts -= 1
        attempts_label.config(text=f"Attempts left: {attempts}")
    
    guess_entry.delete(0, tk.END)
    
    # Check if the player has won or lost
    if "_" not in display_word:
        messagebox.showinfo("Congratulations!", "You guessed the word!")
        start_game()
    elif attempts == 0:
        messagebox.showinfo("Game Over", f"You lost! The word was: {word}")
        start_game()

# Function to restart the game
def restart_game():
    global word, display_word, attempts, word_length
    word = None
    display_word = []
    attempts = 10
    word_label.config(text="")
    attempts_label.config(text="Attempts left: 10")
    guess_entry.delete(0, tk.END)
    length_entry.delete(0, tk.END)
    word_length = None  # Reset word length variable
    guess_entry.focus()

# Create the main window
root = tk.Tk()
root.title("Guess the Word Game")

# Create and place the widgets
length_label = tk.Label(root, text="Enter Word Length (3 to 8):", font=("Arial", 14))
length_label.pack(pady=10)

length_entry = tk.Entry(root, font=("Arial", 14), width=3)
length_entry.pack(pady=5)

start_button = tk.Button(root, text="Start Game", font=("Arial", 14), command=start_game)
start_button.pack(pady=20)

word_label = tk.Label(root, text="", font=("Arial", 24))
word_label.pack(pady=20)

attempts_label = tk.Label(root, text="Attempts left: 10", font=("Arial", 16))
attempts_label.pack()

guess_label = tk.Label(root, text="Enter a letter:", font=("Arial", 14))
guess_label.pack(pady=10)

guess_entry = tk.Entry(root, font=("Arial", 14), width=3)
guess_entry.pack()

guess_button = tk.Button(root, text="Guess", font=("Arial", 14), command=make_guess)
guess_button.pack(pady=20)

# Restart Button
restart_button = tk.Button(root, text="Restart Game", font=("Arial", 14), command=restart_game)
restart_button.pack(pady=10)

# Start the GUI event loop
root.mainloop()


