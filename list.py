#!/bin/bash/python3

import random

nl = [5, 6, 4, 8, 9, 4]
total = 0
large = nl[0]
smail = nl[0]
start = 0
end = 8
count = 0
el_rand_num = 3

#list summer

for i in nl:
    total = total + i

print('list sum: ', total)


#list elements multiply

for i in nl:
    total  = total * i
print('list multuply: ', total)


#largest number

for i in nl:
    if i > large:
        large = i
print('Large element: ',large)


#smail number

for i in nl:
    if i < smail:
        smail = i
print('Smail element: ', smail)


#list count

for i in nl[::1]:
    if start <= i <= end:
        count += 1

print('Count list element: ',count)



#random numebr from list 

rand_list_el = random.sample(nl, el_rand_num)
print('Extract list: ',rand_list_el)


#grid 3x3 list

grid = []

for i in range(3):
    row = [1, 2, 3]
    grid.append(row)

print('List grid list: ',grid)


#remove elemtn from list

original_list = [1, 1, 2, 3, 4, 4, 5, 1]

k = 2

update = original_list[:k] + original_list[k+1:]

print("Original list:", original_list)
print(f"Update list:  {update} ")


# count list of list

nl = [[1, 3], [5, 7], [9, 11], [13, 15, 17]]

for i in nl:
    if type(i) == list:
        count += 1

print("Original list: ", nl)
print("Count of list of lists: ", count)


#check domain

url = "https://www.w3resource.net"
nl = ['.com', '.edu', '.tv']
result = False

for i in nl:
    if i in url:
        result = True
        break

print("Original list:", url, nl)
print(f"Check if {url} contains an element, which is present in the list ")
print(result)

