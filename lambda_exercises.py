''' 1)
Write a Python program to filter a list of integers using Lambda. Go to the editor
Original list of integers:
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Even numbers from the said list:
[2, 4, 6, 8, 10]
Odd numbers from the said list:
[1, 3, 5, 7, 9]
'''

integers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_list = list(filter(lambda num:(num % 2 == 0), integers)) 
print(even_list)
odd_list = list(filter(lambda num:(num % 2 != 0), integers))
print(odd_list) 

''' 2)
find which days of the week have exactly 6 characters.
'''

weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

weekdays_6 = list(filter(lambda x: (len(x) == 6), weekdays))
print(weekdays_6)




''' 3)
remove specific words from a given list 
Original list:
['orange', 'red', 'green', 'blue', 'white', 'black']

Remove words:
['orange', 'black']

After removing the specified words from the said list:
['red', 'green', 'blue', 'white']

'''

original_list = ['orange', 'red', 'green', 'blue', 'white', 'black']
remove_words = ['orange', 'black']
new_list  = list(filter(lambda x: (x not in remove_words), original_list))
print(new_list)






''' 4)
 remove all elements from a given list present in another list
Original lists:
list1: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list2: [2, 4, 6, 8]

Remove all elements from 'list1' present in 'list2:
[1, 3, 5, 7, 9, 10]
 '''

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list2 = [2, 4, 6, 8]
list3  = list(filter(lambda x: (x not in list2), list1))
print(list3)



''' 5)
find the elements of a given list of strings that contain specific substring using lambda
Original list:
['red', 'black', 'white', 'green', 'orange']
Substring to search:
ack
Elements of the said list that contain specific substring:
['black']
Substring to search:
abc
Elements of the said list that contain specific substring:
[]

'''

Original_list = ['red', 'black', 'white', 'green', 'orange']
str1 = 'ack'
list4 = list(filter(lambda x: (str1 in x), Original_list))
print(list4)
str2 = 'abc'
list5 = list(filter(lambda x: (str2 in x), Original_list))
print(list5)

''' 6)
check whether a given string contains a capital letter, a lower case letter, a number and a minimum length of 8 characters.
(This is like a password verification function, HINT: Python function 'any' may be useful)
'''

def check_string(str1):
    message = [
    lambda str1: any(x.isupper() for x in str1) or 'Password must have 1 upper case character.',
    lambda str1: any(x.islower() for x in str1) or 'Password must have 1 lower case character.',
    lambda str1: any(x.isdigit() for x in str1) or 'Password must have 1 number.',
    lambda str1: len(str1) >= 8                 or 'Password length should be at least 8.',]
    result = [x for x in [i(str1) for i in message] if x != True]
    if not result:
        result.append('Valid password.')
    return result    
s = input("Input the password: ")
print(check_string(s))


''' 7)
Write a Python program to sort a list of tuples using Lambda.

# Original list of tuples:
original_scores = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]

# Expected Result:
# [('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]
'''

original_scores = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
original_scores.sort(key = lambda x: x[1])
print(original_scores)