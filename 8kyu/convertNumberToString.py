#Define function
''' Created a list of integers that will be passed to
    number_to_string function'''
number_list = [1, 2, 3, 4, 5, -12]
''' Defined a function named number_to_string that will 
    take the argument of nums'''
def number_to_string(nums):
    ''' Inside the function the new list of string
        numbers will store the new list'''
    string_number_list = []
    ''' The for loop will iterated through each number
        in the number_list(nums)'''
    for num in nums:
        ''' For each number item in the list
            is converted to a string using the str()
            method and then appended(added to the new list)'''
        string_number_list.append(str(num))
        ''' Once the loop is done it returns the new list'''
    return string_number_list
        

''' returns ['1', '2', '3', '4', etc..] '''
print(number_to_string(number_list))