# Assignment 4:
"""
In the list shown below, replace the letter m with the letter x
and replace the word TV with the word television. Then print my_list.
"""

my_list = [(1, 2), (3, 4), (['c', 'd', 'a', 'm'], [3, 9, 4, 12], 4), 'TV', 42]


# Your Code Below:

third_element=list(my_list[2])
manipulation_1=third_element[0][3]='x'
third_element=tuple(third_element)
fourth_element=my_list[3]='television'
my_list.pop(2)
my_list.insert(2,third_element)




print(my_list)

































# Solution:
# my_list[2][0][3] = 'x'
# my_list[3] = 'Television'
# print(my_list)