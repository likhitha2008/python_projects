# quiz_game.py

score = 0

print("Welcome to the Python Quiz Game!")
print("----------------------------------")

# Question 1
answer = input("1. What keyword is used to define a function in Python? ")

if answer.lower() == "def":
    print("Correct!")
    score += 1
else:
    print("Wrong! The correct answer is 'def'.")

# Question 2
answer = input("2. Which data type is used to store whole numbers? ")

if answer.lower() == "int":
    print("Correct!")
    score += 1
else:
    print("Wrong! The correct answer is 'int'.")

# Question 3
answer = input("3. What symbol is used for comments in Python? ")

if answer == "#":
    print("Correct!")
    score += 1
else:
    print("Wrong! The correct answer is '#'.")

# Final Score
print("\nQuiz Completed!")
print(f"Your final score is: {score}/3")

if score == 3:
    print("Excellent work!")
elif score == 2:
    print("Good job!")
else:
    print("Keep practicing!")