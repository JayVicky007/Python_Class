'''
Define a function called kelvinToFahrenheit to convert temperature from kelvin to Fahrenheit.
The function should have an assert that checks if the temperature is greater or equal to zero,
if not, display a message "Colder than absolute zero".

Formula = (k - 273.15) * 9/5 + 32
'''

def kelvinToFahrenheit(k):
    assert k >= 0, "Colder than absolute zero."
    F = (k - 273.15) * 9/5 + 32

    print(F)

kelvinToFahrenheit(-100)




# def kelvinToFahrenheit(k):
#     assert k >= 0, "Colder than absolute zero."
#     F = (k - 273.15) * 9/5 + 32
#     return F

# temp = -100
# converted_temp = kelvinToFahrenheit(temp)
# print(converted_temp)

















