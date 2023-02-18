#!/bin/bash/python3


#1 solution

#total = 0

#def get_num_sum():
#    total = 0
#    while True:
#        user_input = input("Enter text: ")
#        if user_input.lower() == "stop":
#            print("Total sum:", total)
#            break
#        elif user_input.isalpha():
#            continue
#        elif user_input.isdigit():
#            total += int(user_input)
#
#get_num_sum()


#2 soloition

#def total_lines():
#    count = 0
#    while True:
#        user_input = input("Enter text: ")
#        if user_input.lower() == 'stop':
#            print('Total lines:', count)
#            break
#        else:
#            count += 1
#total_lines()

#3 soloition

#def average(*x):
#    if len(x) == 0:
#        return 0
#    else:
#        return sum(x) / len(x)
#
#result = average(7,8,9,7,5)
#print('Total', result)

#4 soloition

#def operations(x, y):
#    sum_result = x + y
#    
#    diff_result = x - y
#    
#    mult_result = x * y
#    
#    div_result = x / y
#    
#    floor_div_result = x // y
#    
#    mod_result = x % y
#    
#    exp_result = x ** y
#    
#    # print the results
#    print("Sum:", sum_result)
#    print("Difference:", diff_result)
#    print("Product:", mult_result)
#    print("Quotient:", div_result)
#    print("Floor division:", floor_div_result)
#    print("Modulus:", mod_result)
#    print("Exponentiation:", exp_result)
#    
#    return (sum_result, diff_result, mult_result, div_result, floor_div_result, mod_result, exp_result)
#
#operations(10,5)

#5 solotion

#def to_uppercase():
#    string = input('Enter text: ')
#    uppercase = ''
#    for i in string:
#        if ord('a') <= ord(i) <= ord('z'):
#            uppercase += chr(ord(i) - 32)
#        else:
#            uppercase += i
#    return uppercase
#
#uppercase_string = to_uppercase()
#print(uppercase_string)

#6 solotion

#def to_lower_case():
#    string = input("Enter text: ")
#    lowercase = ''
#    for char in string:
#        if ord(char) >= 65 and ord(char) <= 90:
#            lowercase += chr(ord(char) + 32)
#        else:
#            lowercase += char
#    return lowercase
#
#
#lowercase_string = to_lower_case()
#print(lowercase_string)

#7 solotion

#def get_initials(line):
#    words = line.split()
#    for i in range(len(words)):
#        words[i] = words[i][0].upper() + words[i][1:]
#    return " ".join(words)
#user_input = input('Enter text: ')
#result = get_initials(user_input)
#print(result)

#8 solotion

#def reverse_string(string):
#    return ''.join(reversed(string))
#
#string = input('Enter text: ')
#reversed_string = reverse_string(string)
#print(reversed_string)

#9 solotion

#def get_substring(string, start_index, end_index):
#    return string[start_index:end_index]
#
#string = input('Enter text: ')
#start_index = int(input('Enter start index: '))
#end_index = int(input('Enter end index: '))
#substring = get_substring(string, start_index, end_index)
#print(substring)

#10 solotion

#def longest_word(sentence):
#    words = sentence.split()
#
#    longest = words[0]
#
#    for word in words:
#        if len(word) > len(longest):
#            longest = word
#
#    return longest
#
#
#sentence = input('Enter text: ')
#print(longest_word(sentence)) 

#11 solotion

#def most_used_letter(sentence):
#    sentence = sentence.lower()
#    
#    letter_count = {}
#    for letter in sentence:
#        if letter.isalpha():
#            if letter in letter_count:
#                letter_count[letter] += 1
#            else:
#                letter_count[letter] = 1
#    
#    max_count = 0
#    most_used = ''
#    for letter in letter_count:
#        if letter_count[letter] > max_count:
#            max_count = letter_count[letter]
#            most_used = letter
#    
#    return most_used
#
#sentence = input('Enter text: ')
#most_used = most_used_letter(sentence)
#print("Frequently used letter in the sentence is:", most_used)

#12 solotion

#def most_common_letter(sentence):
#    words = sentence.split()
#
#    longest_word = max(words, key=len)
#
#    letter_count = {}
#    for letter in longest_word:
#        if letter not in letter_count:
#            letter_count[letter] = 1
#        else:
#            letter_count[letter] += 1
#
#    most_common = max(letter_count, key=letter_count.get)
#
#    return most_common
#
#user_input = input('Enter text: ')
#result = most_common_letter(user_input)
#print(result)

#13 solotion

#def get_characters_at_index(string, index):
#    if index < 0 or index >= len(string):
#        return ""
#
#    return string[:index+1]
#user_input = input('Enter text: ')
#result = get_characters_at_index(user_input, 5)
#print(result)

#15 solotion


#def is_palindrome(num):
#    if not isinstance(num, int):
#        return False
#    if num < 0:
#        return False
#    num_str = str(num)
#    num_len = len(num_str)
#    for i in range(num_len // 2):
#        if num_str[i] != num_str[num_len - i - 1]:
#            return False
#    return True
#
#while True:
#    user_input = input('Enter a 3-digit number: ')
#    if len(user_input) == 3 and user_input.isnumeric():
#        user_input = int(user_input)
#        break
#    print('Invalid input, please enter a 3-digit number.')
#
#if is_palindrome(user_input):
#    print('Palindrome')
#else:
#    print('Not a palindrome')

#16 solotion


#def closest_polynomial(n):
#    if isinstance(n, int):
#        # If n is already an integer, it is a polynomial number
#        return n
#    else:
#        # Try all polynomial expressions of degree up to 3
#        closest = float('inf')
#        for a in range(-1, 2):
#            for b in range(-1, 2):
#                for c in range(-1, 2):
#                    for d in range(-1, 2):
#                        poly = a*n**3 + b*n**2 + c*n + d
#                        distance = abs(poly - n)
#                        if distance < abs(closest - n):
#                            closest = poly
#        return closest
#
#user_input = float(input('Enter number: '))
#result = closest_polynomial(user_input)
#print(result)

#17 solotion

#def first_last_product(n):
#    num_str = str(n)
#
#    first = int(num_str[0])
#    last = int(num_str[-1])
#
#    return first * last
#
#user_input = int(input('Enter number: '))
#result = first_last_product(user_input)
#print(result) 

#18 solotion

#def count_rows(my_list):
#    return len(my_list)
#
#my_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#num_rows = count_rows(my_list)
#print(num_rows) 

#19 solotion

#def find_max(numbers):
#    
#    max_value = numbers[0] 
#    for num in numbers:
#        if num > max_value:
#            max_value = num
#    return max_value
#
#my_list = [5, 10, 2, 20, 8]
#max_num = find_max(my_list)
#print(max_num)

#20 solotion

#def find_two_digit_evens(new_list):
#    # create an empty list to store the even numbers
#    evens = []
#
#    # loop over each element in the list
#    for num in new_list:
#        # check if the number has two digits and is even
#        if num >= 10 and num <= 99 and num % 2 == 0:
#            # add the number to the even numbers list
#            evens.append(num)
#
#    # return the even numbers list
#    return evens
#my_list = [23, 14, 55, 66, 82, 97, 100]
#evens = find_two_digit_evens(my_list)
#print(evens) # prints [14, 66, 82]

#21 solotion

#def arithmetic_mean(numbers):
#    if len(numbers) == 0:
#        return 0
#    else:
#        return sum(numbers) / len(numbers)
#
#numbers = [1, 2, 3, 4, 5]
#print(arithmetic_mean(numbers))

#22 solotion

#def string_lengths(strings):
#    return [len(s) for s in strings]
#
#strings = ["hello", "world", "python", "programming"]
#lengths = string_lengths(strings)
#print(lengths) 

#23 solotion

#def sort_descending(numbers):
#    return sorted(numbers, reverse=True)
#
#
#my_list = [5, 2, 8, 1, 3]
#sorted_list = sort_descending(my_list)
#print(sorted_list)

#24 solotion

#def sort_lines_descending(lines):
#    sorted_lines = sorted(lines, key=lambda line: len(line), reverse=True)
#    return sorted_lines
#lines = ["This is a short line", "This is a longer line", "This is the longest line of them all"]
#sorted_lines = sort_lines_descending(lines)
#print(sorted_lines)

#25 solotion

#def most_vowels(words):
#    vowels = 'aeiouAEIOU'
#    max_vowel_count = 0
#    max_vowel_word = ''
#
#    for word in words:
#        vowel_count = 0
#        for char in word:
#            if char in vowels:
#                vowel_count += 1
#        if vowel_count > max_vowel_count:
#            max_vowel_count = vowel_count
#            max_vowel_word = word
#
#    return max_vowel_word
#
#words = ['hello', 'world', 'apple', 'banana']
#most_vowel_word = most_vowels(words)
#print(most_vowel_word)

#26 solotion

#def find_sentence_with_most_words(sentences):
#    max_sentence = ''
#    max_words = 0
#    for sentence in sentences:
#        words = len(sentence.split())
#        if words > max_words:
#            max_words = words
#            max_sentence = sentence
#    return max_sentence
#sentences = ["The quick brown fox jumps over the lazy dog.",
#             "The cat in the hat sat on the mat.",
#             "Jack and Jill went up the hill to fetch a pail of water.",
#             "To be or not to be, that is the question."]
#
#result = find_sentence_with_most_words(sentences)
#print(result) 

#27 solotion

#def find_largest_number(sentence):
#    largest_number = None
#    current_number = ""
#
#    for char in sentence:
#        if char.isdigit():
#            current_number += char
#        else:
#            if current_number and (not largest_number or int(current_number) > largest_number):
#                largest_number = int(current_number)
#
#            current_number = ""
#
#    if current_number and (not largest_number or int(current_number) > largest_number):
#        largest_number = int(current_number)
#
#    return largest_number
#
#sentence = "The largest number is 1000, not 100."
#largest_number = find_largest_number(sentence)
#print(largest_number)

#28 solotion

#def oldest_person(people_list):
#    max_age = 0
#    oldest_person_dict = {}
#    for person in people_list:
#        if person['age'] > max_age:
#            max_age = person['age']
#            oldest_person_dict = person
#    return oldest_person_dict
#
#people = [
#    {'name': 'Alice', 'age': 32},
#    {'name': 'Bob', 'age': 45},
#    {'name': 'Charlie', 'age': 28},
#    {'name': 'Dave', 'age': 52}
#]
#
#oldest = oldest_person(people)
#print(oldest)

#29 solotion

#def sort_students_by_units(students):
#    return sorted(students, key=lambda x: x['units'])
#
#students = [
#    {'name': 'Alice', 'units': 20},
#    {'name': 'Bob', 'units': 10},
#    {'name': 'Charlie', 'units': 30},
#    {'name': 'David', 'units': 15}
#]
#
#sorted_students = sort_students_by_units(students)
#print(sorted_students)

#30 solotion

# def get_longest_university(universities):

#     longest_uni = None
#     longest_len = 0

#     for uni in universities:
#         name_len = len(uni['name'])
#         if name_len > longest_len:
#             longest_len = name_len
#             longest_uni = uni

#     return longest_uni


# universities = [
#     {'name': 'Massachusetts Institute of Technology'},
#     {'name': 'California Institute of Technology'},
#     {'name': 'Stanford University'},
#     {'name': 'Harvard University'},
#     {'name': 'Princeton University'},
# ]

# longest_uni = get_longest_university(universities)

# print(longest_uni)

