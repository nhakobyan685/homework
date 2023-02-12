#!/bin/bash/python3.10


import random

# Define a list of 20 questions
questions = [
    {"question": "5 * 2?", "options": ["2", "15", "10"], "answer": "3"},
    {"question": "7 * 3?", "options": ["24", "21", "27"], "answer": "2"},
    {"question": "8 * 4?", "options": ["32", "36", "40"], "answer": "1"},
    {"question": "9 * 5?", "options": ["50", "45", "55"], "answer": "2"},
    {"question": "10 * 6?", "options": ["70", "65", "60"], "answer": "3"},
    {"question": "11 * 7?", "options": ["91", "84", "77"], "answer": "3"},
    {"question": "12 * 8?", "options": ["96", "104", "112"], "answer": "1"},
    {"question": "13 * 9?", "options": ["117", "126", "135"], "answer": "1"},
    {"question": "14 * 10?", "options": ["160", "150", "140"], "answer": "3"},
    {"question": "15 * 11?", "options": ["176", "165", "187"], "answer": "2"},
    {"question": "16 * 12?", "options": ["205", "192", "216"], "answer": "2"},
    {"question": "17 * 13?", "options": ["221", "234", "247"], "answer": "1"},
    {"question": "18 * 14?", "options": ["281", "266", "252"], "answer": "3"},
    {"question": "19 * 15?", "options": ["306", "285", "323"], "answer": "2"},
    {"question": "20 * 16?", "options": ["365", "336", "320"], "answer": "3"},
    {"question": "21 * 17?", "options": ["357", "378", "399"], "answer": "1"},
    {"question": "22 * 18?", "options": ["396", "420", "444"], "answer": "1"},
    {"question": "23 * 19?", "options": ["447", "437", "487"], "answer": "2"},
    {"question": "24 * 20?", "options": ["526", "500", "480"], "answer": "3"}
]


# questions = []
# with open('questions.txt', 'r') as f:
#     for i in f:
#         questions.append(eval(o.strip()))


# Select 10 random questions from the list
selected_questions = random.sample(questions, 10)

# Keep track of the number of correct answers
correct_answers = 0

for question in selected_questions:
    print(question["question"])
    for i, option in enumerate(question["options"]):
        print(f"{i+1}) {option}")
    user_input = input("Enter your answer: ")
    if user_input == question["answer"]:
        print("Correct!")
        correct_answers += 1
    else:
        print("Incorrect.")
    print()

print(f"You answered {correct_answers} out of {len(selected_questions)} questions correctly.")

f = open('usertop.txt', 'w')
print(f.write(f'Top user: {name}'))
f.close()


