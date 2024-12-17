import random
from validate_words import Validate
import subprocess #to run the different files


#Remember to give the user a choice to either play in terminal or GUI mode
# 0 for terminal, and 1 for GUI mode


def user_input_validation():

    while True: #To prompt the user to enter a number until it's valid
        try: #Use try & except to account for input that is not an integer 
            user_input = input("Please enter the length of the word: ")
            length = int(user_input)

            if 3 <= length <= 8:
                return length

            else:
                print("Kindly pick a number between 3 and 8")
               
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def get_random_word(word_length):

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

    if word_length == 3:
        word = random.choice(three_letter_word_list)
        print("A random word has been generated.")
        return word

    elif word_length == 4:
        word = random.choice(four_letter_word_list)
        print("A random word has been generated.")
        return word

    elif word_length == 5:
        word = random.choice(five_letter_word_list)
        print("A random word has been generated.")
        return word

    elif word_length == 6:
        word = random.choice(six_letter_word_list)
        print("A random word has been generated.")
        return word

    elif word_length == 7:
        word = random.choice(seven_letter_word_list)
        print("A random word has been generated.")
        return word

    else:
        word = random.choice(eight_letter_word_list)
        print("A random word has been generated.")
        return word

def check_word(word, word_length):

    attempt = 10 #After attempt reaches 0, end game, user has to restart.

    while attempt >= 0:

        user_input = input("Kindly input your guess for the word: ")

        if len(user_input) != len(word):
            print("Kindly enter the accurate number of letters.")
        else:
            while word_length > 0:
                if word_length == 3:
                    three_letter_word = Validate.validate_3_letter_word(user_input, word)
                    if three_letter_word is True:
                        exit()
                    break

                elif word_length == 4:
                    four_letter_word = Validate.validate_4_letter_word(user_input, word)   
                    if four_letter_word is True:
                        exit()
                    break
                        
                elif word_length == 5:
                    five_letter_word = Validate.validate_5_letter_word(user_input, word)
                    if five_letter_word is True:
                        exit()
                    break

                elif word_length == 6:
                    six_letter_word = Validate.validate_6_letter_word(user_input, word)
                    if six_letter_word is True:
                        exit()
                    break

                elif word_length == 7:
                    seven_letter_word = Validate.validate_7_letter_word(user_input, word)
                    if seven_letter_word is True:
                        exit()
                    break

                elif word_length == 8:
                    eight_letter_word = Validate.validate_8_letter_word(user_input, word)
                    if eight_letter_word is True:
                        exit() 

                    word_length -= 1
                    break
                else:
                    break

        attempt -= 1

        if attempt == 0:
            print(f"You lost. The correct word was {word}")
            break
        else:
            print(f"You have {attempt} attempts left.")

if __name__=="__main__":

    while True:
        # Check for command-line arguments
        mode = input("Please enter mode of the game: 0 for terminal or 1 for GUI. ")
        if mode == "0":  # Terminal mode
            # Run the terminal game file
            word_length = user_input_validation()
            word = get_random_word(word_length)
            check_word(word, word_length)
            break

        elif mode == "1":  # GUI mode
            # Run the GUI game file
            subprocess.run(["python", "GUI_gtw.py"])
            break
            
        else:
            print("Invalid mode. Use 0 for terminal or 1 for GUI.")

