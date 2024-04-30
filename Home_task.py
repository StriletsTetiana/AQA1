
#Home task 2
print('Home task2\nCreate list of 3 cats/dogs names \nOutput elements using coma and space: ')
pet_names_list=['Murzik', 'Barsik', 'Pantera']
print(pet_names_list[0] , pet_names_list[1], pet_names_list[2], sep=',')



#Home task 3 Part_1
print ('\nHome task 3 \nCreate list of 3 countries names.')
list_of_country=['Ukraine', 'Poland', 'Spaine']
print (list_of_country)

#Part_2 Create dictionary of 3 key-value pairs.
# Part_3 Key should be country name from the list and value should be string with its capital.
dictionary_countries= {
    'Ukraine': 'Kyiv',
    'Poland': 'Warsaw',
    'Spaine': 'Madrid'
}

print ('\nCreate dictionary of 3 key-value pairs.\nOutput each pair on separate lines. Separate key from value with colon and space')
for key, value in dictionary_countries.items():
    print(key, value, sep=':')
#see details solution https://stackoverflow.com/questions/3545331/how-can-i-get-dictionary-key-as-variable-directly-in-python-not-by-searching-fr

#Home task 4
print ('\nHome task 4.\nUser input processing Request two integer numbers from user. \nOutput on one line expression with sum of numbers, and on another line - expression with product of numbers:')

first_number = input('Enter first number')
first_number= int(first_number)
second_number = input('Enter second_number')
second_number=int(second_number)
_Sum_of_numbers= first_number + second_number
_Product_of_numbers =first_number*second_number

print (f'Sum of numbers {_Sum_of_numbers}')
print (f'Product of numbers {_Product_of_numbers}')

#Home task 5
print ('\nHome task5. Maximum number\n Output the maximum number of 3 user-entered numbers.\nDO NOT use built-in functions. Use only flow control instructions (ifs, loops)')
first_number = input('Enter first number')
first_number = int(first_number)
second_number = input('Enter second number')
second_number = int(second_number)
third_number = input('Enter third number')
third_number = int(third_number)
if (first_number > second_number) and (first_number> third_number):
    print(f'The greatest number is {first_number}')
elif (second_number > first_number) and (second_number > third_number):
    print(f'The greatest number is {second_number}')
else:
    print(f'The greatest number is {third_number}')


#Home task 6 Rectangle output
print ('User enters height and width of rectangle (integer numbers), and any symbol.\nOutput a rectangle made up of the entered character of a given size.\nThere are NO spaces at the end of lines.\n')
height = int(input('Enter height of rectangular:'))
width = int(input('Enter width of rectangular:'))
symbol = input('Enter symbol to build rectangular with:')

for i in range(height):
    print(symbol * width)


#Home task 7 Triangle output
print('Output a triangle of user-entered size.\nThere are NO spaces at the end of lines.\nDO NOT use methods of string type.\n')

#First_option
variable_1 = 1
triangle_size = int(input('Please, enter triangle size:'))
while variable_1 < triangle_size:
   print(variable_1 * '*')
   variable_1 += 1
else:
    print(triangle_size * '*')

#Second_option
for t in range(triangle_size):
    print(t * '*')
    variable_1 += 1
else:
    print(triangle_size * '*')




#Home_task_10 Palindrome
#The user enters a string. Print True if the string is a palindrome, otherwise False.
# A palindrome is a string that reads the same way from the left and from the right.
#If there are leading or trailing spaces in the line, they should not be taken into account

#First option
def isPalindrom(string):
    string = string.lower()
    if (string==string[::-1]):
        return 'True'
    else:
        return 'False'
string=input('Enter data for checking whether the word is palindrome or not:')
print(isPalindrom(string))


#Second option
palindrom_2= input ("Enter data for checking whether the word is palindrome or not:")
rev_str= ''
for i in palindrom_2:
    rev_str= i + rev_str
if palindrom_2.lower() == rev_str.lower():
    print('True')
else:
    print('False')


# 11. Number of words in sentence
#The program has a string `sentences`.
#The string consists of sentences.
#A 'sentence' is a set of characters delimited by periods(. or ...) or the beginning of a line and a period.
#Return list with number of words in each sentence.
#A 'word' is a set of characters between two spaces or the beginning of a line and a space.
#DO NOT use regular expressions.

text = input('Enter your text for cheking count of words in sentence: ')
count_of_words = []
count = 0
for word in text.split():
    count = count + 1
    if word.endswith('.') or word.endswith('...'):
        count_of_words.append(count)
        count = 0
print(count_of_words)

#Home task 12.Search words by condition
#The program has a line `string`.
#Print the all words, containing the letter 'o' (in any case (upper/lower)) twice, as a title.

string = "This tool is cool. But that owl is awful. MAGIC TOOLS Ltd."

result = ""
for word in string.split():
    if word.lower().find('oo') != -1:
        result = result + word.title() + " "
print(result)



'''Home_task_14_List separation
There is a list consisting of integer numbers.
Create three lists:
- to the first list add numbers that are only divisible by 3, but not divisible by 5
- to the second list add numbers that are divisible by 5, but not divisible by 3
- to the third list add numbers that are divisible by both 3 and 5
'''

list_with_some_numbers = [] # creating an empty list
n = int(input("Enter number of elements inside the list: ")) # number of elements as input

for i in range(0, n):
    ele = int(input())
    list_with_some_numbers.append(ele) # adding the element
print('The full list:')
print(list_with_some_numbers)

new_list_3 =[]
new_list_5 =[]
new_list_3_and_5 =[]

for x in list_with_some_numbers:
    if x % 3 ==0 and x % 5 !=0:
        new_list_3.append(x)
print ('The first list add numbers that are only divisible by 3, but not divisible by 5')
print(new_list_3)

for x in list_with_some_numbers:
    if x % 5 == 0 and x % 3 != 0:
      new_list_5.append(x)

print('The second list add numbers that are divisible by 5, but not divisible by 3')
print(new_list_5)
for x in list_with_some_numbers:
    if x % 5 == 0 and x % 3 == 0:
       new_list_3_and_5.append(x)
print('The third list add numbers that are divisible by both 3 and 5')
print(new_list_3_and_5)
