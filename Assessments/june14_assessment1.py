'''
1. Write a function called "multiply_even_numbers" that takes in a list of numbers as a parameter and 
returns the product of all even numbers in the list. If there are no even numbers in the list, return 1.

2. Write a program that takes a list of words as input and returns a new list containing only 
the words that have more than 4 characters

3. Write a function called "count_positive_negative" that counts the numbers of 
positive and negative numbers in the list. The function should return a tuple with two elements: 
the count of positive numbers and the count of negative numbers.

'''

def multiply_even_numbers(numbers):
    product = 1

    for num in numbers:
        if num % 2 == 0:
            product *= num
        else:
            product *= 1
    return product

mult_even = multiply_even_numbers([1,2,3,4,5,6,7,8,9,10])
# mult_even = multiply_even_numbers([1,11,3,13,5,15,7,17,9,21])
print(mult_even)