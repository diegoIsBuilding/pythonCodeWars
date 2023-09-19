#The fastest and easiest way to reverse a string is by using 'slice'
#that steps backwards
testString = 'Diego'

#def reversedString(string):
    #return string[::-1] #This does not work because it returns a 
#reversed list. The strings in the list are still normal


#print(reversedString(listOfStrings))
#def reversedString(string):
#    for string in listOfStrings:
#        return string[::-1] #This returns only the first string item in
    #the list reversed 
    
#print(reversedString(listOfStrings))

#Reverse a string using slicing
def reversedString(string): #the function takes a string parameter
  return string[::-1] #slicing starts with start position and end position
  
#'string' is the input string that you want to reverse
#'[::]' is Python's slice notation - usually take three parameters
#'[start:stop:step]' 
#'start' - this is the index where the slice starts
#'stop' - this is the index where the slice stops
#'step' - this is how you move from the 'start' index to the 'stop' index

#'[::-1]' - this is a slice with no start or stop defined and step of -1. 
#A step of -1 means take each item in reverse order

#so 'string[::-1] reverses the input string by taking all characters from 
#start to end in reverese
print(f'Reversed String using {reversedString(testString)}') 


testForLoopString = 'Garcia'
#Reverese String using For Loop
def reversedStringForLoop(string):
  reversedString = '' #The function starts by creating an empty string called s1
  for character in string: #This tells python to loop through each character in the string
    reversedString = character + reversedString #This builds the reverse string - the function puts each character
    #in front of what is already in the string --> so if it already has 'G' then it put 'a' in front like this
    #'aG' then 'raG' and so on
  return reversedString #once the loop is finsihed the function returns the reversed string

  
  
print(f'The string was reveresed using a for loop {reversedStringForLoop(testForLoopString)}')

testStringWhileLoop = 'Daisy'
#Reverse a string using While Loop
def whileLoopReverse(string):
  reversedString = '' #First an empty string called reveresedString is created
  #this is where the reversed string is built
  lengthOfString = len(string) - 1 #This gets the length of the input string
  #and subtracts 1 to get the 'lengthOfString' - In python string indices start at 0
  #so the last character is 1 less than the strings length
  print(len(testStringWhileLoop)) #Returns 5
  
  while lengthOfString >= 0: #This tells python to loop until the lengthOfString 
    #is greater than or equal to zero - this means it will loops from the last charater
    #in the string to the first character in the string
    reversedString = reversedString + string[lengthOfString] #In each loop iteration
    #the function will take a character from the end of the string --string[lengthOfString]
    #and add it to the reversedString
    lengthOfString = lengthOfString - 1 #lengthOfString is reduced by 1 - this moves
    #the index to the previous character in the string - so from index 4 to index 3 to index 2 and so on
  return reversedString #once the loop is done the function returns the reversed string

print(f'Reversed using a while loop {whileLoopReverse(testStringWhileLoop)}')