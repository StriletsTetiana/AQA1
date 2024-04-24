
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





