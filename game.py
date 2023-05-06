print("Welcome to State Capitals Trivia!")

print('Enter your name: ')
user_name = input()
print(f'Welcome, {user_name}! Type the capital for each state randonly selected and press enter. You may also type score at any time to check your score, or quit to exit the game. Good luck!')

import random

states = ['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming']

capitals = ('Montgomery', 'Juneau', 'Phoenix', 'Little Rock', 'Sacramento', 'Denver', 'Hartford', 'Dover', 'Tallahassee', 'Atlanta', 'Honolulu', 'Boise', 'Springfield', 'Indianapolis', 'Des Moines', 'Topeka', 'Frankfort', 'Baton Rouge', 'Augusta', 'Annapolis', 'Boston', 'Lansing', 'Saint Paul', 'Jackson', 'Jefferson City', 'Helena', 'Lincoln', 'Carson City', 'Concord', 'Trenton', 'Santa Fe', 'Albany', 'Raleigh', 'Bismarck', 'Columbus', 'Oklahoma City', 'Salem', 'Harrisburg', 'Providence', 'Columbia', 'Pierre', 'Nashville', 'Austin', 'Salt Lake City', 'Montpelier', 'Richmond', 'Olympia', 'Charleston', 'Madison', 'Cheyenne')

# Match the state with capital before randomizing
    # loop through the states  and capitals using i to assign index
state_capital = {states[i]: capitals[i] for i in range(len(states))}

# Shuffle the states
random.shuffle(states)
score = 0

# correct and incorrect keys
correct = 0
incorrect = 0

# loop through randomized states and ask for state capital
for state in states:
    # get the state index for the randonly selected state to assign to the capital
    capital = state_capital[state] # capital = the corresponding state in the dict created pairing the state[i] = capital[i]
    user_input = input(f"What is the capital of {state}? ")
    # check if the answer input matches the capital
    if user_input == capital:
        # add 1 to score
        score += 1
        correct += 1
        print(f"Good job, {user_name}! You earned a point for knowing the capital of {state}.")
    # Allow user to check score during game
    elif user_input == 'score':
        print(f'Score: {score}')
    # Allow user to leave the game
    elif user_input == 'quit':
        print('Thanks for playing!')
        break
    else:
        incorrect += 1
        print(f"Incorrect.. The correct answer is {capital}. Here's another shot:")

# print final score when user types 'quit' and break runs
print(f'Final Correct Count: {correct}')
print(f'Final Incorrect Count: {incorrect}')
print(f'Final Score: {score}')







