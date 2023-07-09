# Assignment 1:
"""
Print Bill's salary from the my_list object shown below.

my_list = [{'Tom': 20000, 'Bill': 12000}, ['car', 'laptop', 'TV']]

"""

my_list = [{'Tom': 20000, 'Bill': 12000}, ['car', 'laptop', 'TV']]
# your code below:
bill_salary=my_list[0]['Bill']

print(f'The Salary that {list(my_list[0].keys())[1]} earns is $ {bill_salary}')






































# Solution
# print(my_list[0].get('Bill'))
