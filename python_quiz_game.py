# Python quiz game
# Declare all the Collections and variables we will need:
# We need a Tuple of questions,a 2D tuple of options
# I will have five questions, but you need to have 12
# It will also have a tuple of answers.
# There will be list of guesses so we can append our list.

# There will be these variables:
# score set to 0
# question_num to keep track of what number question we are on

# Begin with questions

questions = ("How many elements are in the periodic table?: ",
             "Which animal lays the largest eggs?: ",
             "What is the most abundant gas in Earth's atmosphere?: ",
             "How many bones are in the human body?: ",
             "Which planet in the solar system is the hottest?: ")


# 2D Tuple of options - 4 for every question as each inner
# Tuple will have four elements
"""options = ((), this first element corresponds to the first question 
             (),corresponds to 2nd question
             (),corresponds to 3rd question
             ()) corresponds to 4th question"""

options = (("A. 116", "B. 117", "C. 118", "D. 119"),
           ("A. Whale", "B. Crocodile", "C. Elephant", "D. Ostrich"),
           ("A. Nitrogen", "B. Oxygen", "C. Carbon-Dioxide", "D. Hydrogen"),
           ("A. 206", "B. 207", "C. 208", "D. 209"),
           ("A. Mercury", "B. Venus", "C. Earth", "D. Mars"))

answers = ("C", "D", "A", "A", "B")
guesses = []
score = 0
question_num = 0

# Now we display each question
# We can iterate over a Tuple of questions as they are iterable
for question in questions:
    print("----------------------")  # Decorative Text
    print(question)         # after we display every question we need to
    # display every option
